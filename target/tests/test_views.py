import datetime

import pytest
import simplejson
from django.urls import reverse

from book.tests.factories import BookFactory
from common.tests.utils import get_login_params_dict
from custom_user.tests.factories import UserFactory
from target.models import Target
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


@pytest.mark.django_db
class TestTargetDetailView(object):
    def test_target_detail_view_get_detail_target(self, client):
        reward_params = {
            'title': 'test',
            'description': 'test test',
        }

        reward = TargetFactory.create(**reward_params)

        rewards_url = reverse('targets-detail', args=[reward.id])

        resp = simplejson.loads(client.get(rewards_url).content)

        assert resp['title'] == reward_params['title']
        assert resp['description'] == reward_params['description']

    def test_not_owner_can_not_change_target(self, client):
        targets_url = reverse('targets-list')

        user_params_owner = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        user_params_not_owner = {
            'username': 'test_not_owner',
            'email': 'test@test2.com',
            'password': 'test'
        }
        book = BookFactory.create()
        end_date = datetime.datetime.now() + datetime.timedelta(days=21)

        targets_create_params = {
            'title': 'Test title',
            'description': 'test',
            'book': book.id,
            'start_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
        }

        UserFactory.create(**user_params_owner)
        UserFactory.create(**user_params_not_owner)

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        client.post(targets_url, simplejson.dumps(targets_create_params), **token_dict_owner)

        created_target = Target.objects.get(title='Test title')
        targets_detail = reverse('targets-detail', args=[created_target.id])

        user_params_not_owner.pop('email')
        token_dict_not_owner = get_login_params_dict(client, user_params_not_owner)

        resp = simplejson.loads(
            client.put(
                targets_detail, simplejson.dumps({'name': 'new'}), **token_dict_not_owner
            ).content
        )

        expected_resp = {'detail': 'You do not have permission to perform this action.'}

        assert resp == expected_resp

    def test_owner_can_change_target(self, client):
        targets_url = reverse('targets-list')
        user_params_owner = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }
        book = BookFactory.create()
        end_date = datetime.datetime.now() + datetime.timedelta(days=21)
        targets_create_params = {
            'title': 'Test title',
            'description': 'test',
            'book': book.id,
            'start_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
        }

        new_title = 'test_new'

        UserFactory.create(**user_params_owner)

        token_dict_owner = get_login_params_dict(client, user_params_owner)
        client.post(targets_url, simplejson.dumps(targets_create_params), **token_dict_owner)

        created_target = Target.objects.get(title='Test title')
        targets_detail = reverse('targets-detail', args=[created_target.id])

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        resp = simplejson.loads(
            client.patch(
                targets_detail, simplejson.dumps({'title': new_title}), **token_dict_owner
            ).content
        )

        assert resp.get('title') == new_title
