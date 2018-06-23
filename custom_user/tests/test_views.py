import pytest
import simplejson

from django.contrib.auth import get_user_model
from django.urls import reverse

from custom_user.tests.factories import UserFactory
from common.tests.utils import get_login_params_dict


UserModel = get_user_model()


@pytest.mark.django_db
class TestCustomUsersView(object):
    def test_registration_should_be_valid_and_create_user(self, client):
        user_list_url = reverse('users-list')
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        resp = simplejson.loads(client.post(user_list_url, params).content)

        user = UserModel.objects.get(username=params.get('username'))

        assert resp.get('username') == params.get('username')
        assert resp.get('email') == params.get('email')

        assert params.get('username') == user.username

    def test_registration_should_be_invalid_if_email_with_wrong_format(self, client):
        user_list_url = reverse('users-list')
        params = {
            'username': 'test',
            'email': 'test....test.com',
            'password': 'test'
        }
        resp = simplejson.loads(client.post(user_list_url, params).content)
        expected_resp = {'email': ['Enter a valid email address.']}
        assert resp == expected_resp

    def test_registration_should_be_invalid_if_email_is_empty(self, client):
        user_list_url = reverse('users-list')
        params = {
            'username': 'test',
            'email': ' ',
            'password': 'test'
        }
        resp = simplejson.loads(client.post(user_list_url, params).content)
        expected_resp = {'email': ['This field may not be blank.']}

        assert resp == expected_resp

    def test_registration_should_be_invalid_if_empty_password(self, client):
        user_list_url = reverse('users-list')
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': ' '
        }
        resp = simplejson.loads(client.post(user_list_url, params).content)
        expected_resp = {'password': ['This field may not be blank.']}
        assert resp == expected_resp

    def test_registration_should_be_invalid_if_empty_username(self, client):
        user_list_url = reverse('users-list')
        params = {
            'username': ' ',
            'email': 'test@test.com',
            'password': '123321'
        }
        resp = simplejson.loads(client.post(user_list_url, params).content)
        expected_resp = {'username': ['This field may not be blank.']}
        assert resp == expected_resp

    def test_should_return_three_users(self, client):
        user_list_url = reverse('users-list')
        users_count = 3

        UserFactory.create(password='test_1')
        UserFactory.create(password='test_2')
        UserFactory.create(password='test_3')

        resp = simplejson.loads(client.get(user_list_url).content)

        assert users_count == len(resp)

    def test_returned_fields(self, client):
        user_list_url = reverse('users-list')

        UserFactory.create(password='test_1')

        resp = simplejson.loads(client.get(user_list_url).content)
        
        fields = resp[0].keys()
        expected_fields = [
            'username', 'first_name', 'last_name', 'bio', 'country', 'city', 'birth_date', 'favorite_books', 'targets'
        ]
        
        assert list(fields) == expected_fields

    def test_should_not_return_superuser_in_response(self, client):
        user_list_url = reverse('users-list')

        UserFactory.create(username='su', password='test', is_superuser=True)
        UserFactory.create(username='not_su', password='test_2', is_superuser=False)

        resp = simplejson.loads(client.get(user_list_url).content)
        resp_user_names = [resp_obj.get('username') for resp_obj in resp]

        assert 'su' not in resp_user_names


@pytest.mark.django_db
class TestCustomUsersDetailView(object):
    def test_city_should_be_changed_after_put_request(self, client):
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        UserFactory.create(**params)
        user = UserModel.objects.get(username='test')

        user_detail = reverse('users-detail', args=[user.id])

        users_city_before = user.city

        params.pop('email')
        
        token_dict = get_login_params_dict(client, params)

        client.put(
            user_detail, simplejson.dumps({'city': 'New city'}), **token_dict
        )

        user = UserModel.objects.get(username='test')
        users_city_after = user.city

        assert users_city_before != users_city_after

    def test_email_should_not_be_changed_after_put_request(self, client):
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

        UserFactory.create(**params)
        user = UserModel.objects.get(username='test')
        user_detail = reverse('users-detail', args=[user.id])

        users_email_before = user.email

        params.pop('email')

        token_dict = get_login_params_dict(client, params)

        client.put(
            user_detail, simplejson.dumps({'email': 'new@new.ua'}), **token_dict
        )

        user = UserModel.objects.get(username='test')
        users_email_after = user.email

        assert users_email_before == users_email_after

    def test_not_owner_can_not_change_user_profile(self, client):
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        params_1 = {
            'username': 'test_not_owner',
            'email': 'test@test2.com',
            'password': 'test'
        }
        UserFactory.create(**params)
        UserFactory.create(**params_1)
        user = UserModel.objects.get(username='test')

        user_detail = reverse('users-detail', args=[user.id])

        params_1.pop('email')
        token_dict = get_login_params_dict(client, params_1)

        resp = simplejson.loads(
            client.put(
                user_detail, simplejson.dumps({'email': 'new@new.ua'}), **token_dict
            ).content
        )
        expected_resp = {'detail': 'You do not have permission to perform this action.'}

        assert resp == expected_resp

    def test_owner_can_change_user_profile(self, client):
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test',
            'city': 'Kyiv',
        }
        new_city = 'Lviv'
        UserFactory.create(**params)
        user = UserModel.objects.get(username='test')

        user_detail = reverse('users-detail', args=[user.id])

        token_dict = get_login_params_dict(client, params)

        resp = simplejson.loads(
            client.put(
                user_detail, simplejson.dumps({'city': new_city}), **token_dict
            ).content
        )

        assert resp.get('city') == new_city
