import pytest
import simplejson

from django.urls import reverse

from reward.tests.factories import RewardFactory
from common.tests.utils import get_login_params_dict


@pytest.mark.django_db
class TestRewardView(object):
    def test_rewards_list_view_should_return_one_reward(self, client):
        rewards_url = reverse('rewards-list')
        RewardFactory.create()
        
        expected_len = 1
        resp = simplejson.loads(client.post(rewards_url).content)

        assert len(resp) == expected_len

    def test_not_authenticed_users_can_not_add_reward(self, client):
        rewards_url = reverse('rewards-list')
        params = {
            'name': 'laptop',
            'url': 'https://www.test.com/laptop/'
        }

        resp = simplejson.loads(client.post(rewards_url, params).content)
        expected_resp = {'detail': 'Authentication credentials were not provided.'}

        assert resp == expected_resp
