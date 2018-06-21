import pytest
import simplejson

from django.urls import reverse

from book.tests.factories import BookFactory
from common.tests.utils import get_login_params_dict


@pytest.mark.django_db
class TestBooksView(object):
    def test_books_list_view_should_return_one_book(self, client):
        books_url = reverse('books-list')
        BookFactory.create()
        
        expected_len = 1
        resp = simplejson.loads(client.post(books_url).content)

        assert len(resp) == expected_len

    def test_not_authenticed_users_can_not_add_book(self, client):
        books_url = reverse('books-list')
        params = {
            'title': 'Lord of the rings'
        }

        resp = simplejson.loads(client.post(books_url, params).content)
        expected_resp = {'detail': 'Authentication credentials were not provided.'}

        assert resp == expected_resp
    
    def test_authenticed_users_can_add_book(self, client):
        books_url = reverse('books-list')

        params = simplejson.dumps({
            'title': 'Lord of the rings'
        })
        login_params = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

        token_dict = get_login_params_dict(client, login_params)

        resp = simplejson.loads(
            client.post(books_url, params, **token_dict).content
            )     
        expected_resp_title = 'Lord of the rings'

        assert expected_resp_title == resp.get('title')
