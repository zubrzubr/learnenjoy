import pytest
import simplejson

from django.urls import reverse

from book.tests.factories import BookFactory
from custom_user.tests.factories import UserFactory
from common.tests.utils import get_login_params_dict


@pytest.mark.django_db
class TestBooksView(object):
    def test_books_list_view_should_return_three_books(self, client):
        books_url = reverse('books-list')
        BookFactory.create()
        BookFactory.create()
        BookFactory.create()
        
        expected_len = 3
        resp = simplejson.loads(client.get(books_url).content)

        assert len(resp) == expected_len

    def test_books_returned_fields(self, client):
        books_url = reverse('books-list')
        BookFactory.create()
        
        resp = simplejson.loads(client.get(books_url).content)
        resp_keys = resp[0].keys()
        expected_keys = ['id', 'title', 'authors']

        assert expected_keys == list(resp_keys)

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

        UserFactory.create(**login_params)

        token_dict = get_login_params_dict(client, login_params)

        resp = simplejson.loads(
            client.post(books_url, params, **token_dict).content
            )     
        expected_resp_title = 'Lord of the rings'

        assert expected_resp_title == resp.get('title')
