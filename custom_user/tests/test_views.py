import pytest
import simplejson

from django.urls import reverse
from django.contrib.auth import get_user_model


from custom_user.tests.factories import UserFactory


UserModel = get_user_model()


@pytest.mark.django_db
class TestRegistrationView(object):
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

    def test_city_should_be_changed_after_put_request(self, client):
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        UserFactory.create(**params)
        user = UserModel.objects.get(username='test')

        user_detail = reverse('users-detail', args=[user.id])
        user_login = reverse('token_obtain_pair')

        users_city_before = user.city

        params.pop('email')
        resp_login = simplejson.loads(client.post(user_login, params).content)

        token = "Bearer {}".format(resp_login.get('access'))

        client.put(
            user_detail, simplejson.dumps({'city': 'New city'}), content_type='application/json',
            HTTP_AUTHORIZATION=token
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
        user_login = reverse('token_obtain_pair')

        users_email_before = user.email

        params.pop('email')
        resp_login = simplejson.loads(client.post(user_login, params).content)

        token = "Bearer {}".format(resp_login.get('access'))

        client.put(
            user_detail, simplejson.dumps({'email': 'new@new.ua'}), content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        user = UserModel.objects.get(username='test')
        users_email_after = user.email

        assert users_email_before == users_email_after

    def test_only_owner_can_change_user_profile(self, client):
        user_login = reverse('token_obtain_pair')
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
        resp_login = simplejson.loads(client.post(user_login, params_1).content)

        token = "Bearer {}".format(resp_login.get('access'))

        resp = simplejson.loads(
            client.put(
                user_detail, simplejson.dumps({'email': 'new@new.ua'}), content_type='application/json',
                HTTP_AUTHORIZATION=token
            ).content
        )
        expected_resp = {'detail':'You do not have permission to perform this action.'}

        assert resp == expected_resp
