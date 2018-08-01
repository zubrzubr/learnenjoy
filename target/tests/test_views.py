import pytest
import simplejson
from django.urls import reverse

from target.tests.factories import TargetFactory


@pytest.mark.django_db
class TestTargetsView(object):
    def test_targets_view_should_return_three_targets(self, client):
        books_url = reverse('targets-list')

        TargetFactory.create()
        TargetFactory.create()
        TargetFactory.create()

        expected_len = 3

        resp = simplejson.loads(client.get(books_url).content)

        assert len(resp) == expected_len

    def test_targets_returned_fields(self, client):
        books_url = reverse('targets-list')
        TargetFactory.create()

        resp = simplejson.loads(client.get(books_url).content)
        resp_keys = resp[0].keys()

        expected_keys = ['title', 'description', 'book', 'current_page_progress', 'start_date', 'end_date',]

        assert expected_keys == list(resp_keys)
