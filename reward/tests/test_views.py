import pytest
import simplejson

from django.urls import reverse

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

    def test_not_authenticed_users_can_not_add_reward(self, client):
        rewards_url = reverse('rewards-list')
        params = {
            'name': 'laptop',
            'url': 'https://www.test.com/laptop/'
        }

        resp = simplejson.loads(client.post(rewards_url, params).content)
        expected_resp = {'detail': 'Authentication credentials were not provided.'}

        assert resp == expected_resp

    def test_authenticed_users_can_add_reward(self, client):
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
