import mock
import pytest
import simplejson

from django.urls import reverse
from django.contrib.auth import get_user_model


UserModel = get_user_model()


@pytest.mark.django_db
class TestRegistrationView(object):
    def test_registration_view_should_be_valid_and_create_user(self, client):
        registration_url = reverse('users-list')
        params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        resp = simplejson.loads(client.post(registration_url, params).content)

        user = UserModel.objects.get(username=params.get('username'))

        assert resp.get('username') == params.get('username')
        assert resp.get('email') == params.get('email')

        assert params.get('username') == user.username
