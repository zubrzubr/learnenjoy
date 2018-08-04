import datetime

import pytest
import simplejson
from django.urls import reverse

from book.tests.factories import BookFactory
from common.tests.utils import get_login_params_dict
from custom_user.tests.factories import UserFactory
from target.tests.factories import TargetFactory


@pytest.mark.django_db
class TestTargetsView(object):
    def test_targets_view_should_return_three_targets(self, client):
        targets_url = reverse('targets-list')

        TargetFactory.create()
        TargetFactory.create()
        TargetFactory.create()

        expected_len = 3

        resp = simplejson.loads(client.get(targets_url).content)

        assert len(resp) == expected_len

    def test_targets_returned_fields(self, client):
        targets_url = reverse('targets-list')
        TargetFactory.create()

        resp = simplejson.loads(client.get(targets_url).content)
        resp_keys = resp[0].keys()

        expected_keys = ['title', 'description', 'book', 'current_page_progress', 'start_date', 'end_date', 'reward']

        assert expected_keys == list(resp_keys)

    def test_not_authenticated_users_can_not_add_book(self, client):
        targets_url = reverse('targets-list')
        params = {
            'title': 'My target bla bla bla'
        }

        resp = simplejson.loads(client.post(targets_url, params).content)
        expected_resp = {'detail': 'Authentication credentials were not provided.'}

        assert resp == expected_resp

    def test_authenticated_users_can_add_target(self, client):
        targets_url = reverse('targets-list')

        book = BookFactory.create()
        end_date = datetime.datetime.now() + datetime.timedelta(days=21)

        params = simplejson.dumps({
            'title': 'Test title',
            'description': 'test',
            'book': book.id,
            'start_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
        })
        login_params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

        UserFactory.create(**login_params)

        token_dict = get_login_params_dict(client, login_params)
        resp = simplejson.loads(client.post(targets_url, params, **token_dict).content)
        expected_resp_title = 'Test title'

        assert expected_resp_title == resp.get('title')
