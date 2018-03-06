import pytest
import simplejson

from django.urls import reverse
from django.contrib.auth import get_user_model


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
