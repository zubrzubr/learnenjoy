import pytest
import simplejson

from django.urls import reverse

from reward.models import Reward
from reward.tests.factories import RewardFactory
from common.tests.utils import get_login_params_dict
from custom_user.tests.factories import UserFactory


@pytest.mark.django_db
class TestRewardView(object):
    def test_rewards_list_view_should_return_three_rewards(self, client):
        rewards_url = reverse('rewards-list')
        RewardFactory.create()
        RewardFactory.create()
        RewardFactory.create()
        
        expected_len = 3
        resp = simplejson.loads(client.get(rewards_url).content)

        assert len(resp) == expected_len

    def test_rewards_returned_fields(self, client):
        books_url = reverse('rewards-list')
        RewardFactory.create()
        
        resp = simplejson.loads(client.get(books_url).content)
        resp_keys = resp[0].keys()
        expected_keys = ['id', 'name', 'url']

        assert expected_keys == list(resp_keys)

    def test_not_authenticated_users_can_not_add_reward(self, client):
        rewards_url = reverse('rewards-list')
        params = {
            'name': 'laptop',
            'url': 'https://www.test.com/laptop/'
        }

        resp = simplejson.loads(client.post(rewards_url, params).content)
        expected_resp = {'detail': 'Authentication credentials were not provided.'}

        assert resp == expected_resp

    def test_authenticated_users_can_add_reward(self, client):
        rewards_url = reverse('rewards-list')

        params = simplejson.dumps({
            'name': 'laptop',
            'url': 'https://www.test.com/laptop/'
        })
        login_params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

        UserFactory.create(**login_params)

        token_dict = get_login_params_dict(client, login_params)

        resp = simplejson.loads(
            client.post(rewards_url, params, **token_dict).content
            )     

        expected_resp = {
            'id': 1,
            'name': 'laptop',
            'url': 'https://www.test.com/laptop/'
        }

        assert expected_resp == resp


@pytest.mark.django_db
class TestRewardDetailView(object):
    def test_reward_detail_view_get_detail_reward(self, client):
        reward_params = {
            'name': 'test',
            'url': 'https://www.test.com'
        }

        reward = RewardFactory.create(**reward_params)

        rewards_url = reverse('rewards-detail', args=[reward.id])

        resp = simplejson.loads(client.get(rewards_url).content)

        expected_result = dict(reward_params)
        expected_result['id'] = 1

        assert resp == expected_result

    def test_not_owner_can_not_change_reward(self, client):
        rewards_url = reverse('rewards-list')

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

        rewards_create_params = {'name': 'test'}

        UserFactory.create(**user_params_owner)
        UserFactory.create(**user_params_not_owner)

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        client.post(rewards_url, simplejson.dumps(rewards_create_params), **token_dict_owner)

        created_reward = Reward.objects.get(name='test')
        rewards_detail = reverse('rewards-detail', args=[created_reward.id])

        user_params_not_owner.pop('email')
        token_dict_not_owner = get_login_params_dict(client, user_params_not_owner)

        resp = simplejson.loads(
            client.put(
                rewards_detail, simplejson.dumps({'name': 'new'}), **token_dict_not_owner
            ).content
        )

        expected_resp = {'detail': 'You do not have permission to perform this action.'}

        assert resp == expected_resp

    def test_owner_can_change_reward(self, client):
        rewards_url = reverse('rewards-list')

        user_params_owner = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

        rewards_create_params = {'name': 'test', 'url': 'http://www.test.com'}
        new_name = 'test_new'

        UserFactory.create(**user_params_owner)

        token_dict_owner = get_login_params_dict(client, user_params_owner)
        client.post(rewards_url, simplejson.dumps(rewards_create_params), **token_dict_owner)

        created_reward = Reward.objects.get(name='test')
        rewards_detail = reverse('rewards-detail', args=[created_reward.id])

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        resp = simplejson.loads(
            client.put(
                rewards_detail, simplejson.dumps({'name': new_name}), **token_dict_owner
            ).content
        )

        assert resp.get('name') == new_name
