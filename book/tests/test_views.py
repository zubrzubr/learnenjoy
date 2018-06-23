import pytest
import simplejson

from django.urls import reverse

from book.tests.factories import BookFactory, AuthorFactory, GenreFactory
from custom_user.tests.factories import UserFactory
from common.tests.utils import get_login_params_dict
from book.models import Book


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

    def test_not_authenticated_users_can_not_add_book(self, client):
        books_url = reverse('books-list')
        params = {
            'title': 'Lord of the rings'
        }

        resp = simplejson.loads(client.post(books_url, params).content)
        expected_resp = {'detail': 'Authentication credentials were not provided.'}

        assert resp == expected_resp
    
    def test_authenticated_users_can_add_book(self, client):
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


@pytest.mark.django_db
class TestBookDetailView(object):
    def test_books_detail_view_get_detail_book_page(self, client):
        book_params = {
            'title': 'test',
            'page_count': 500,
            'description': 'test_description'
        }
        author_params = {
            'first_name':'John', 
            'last_name':'Dad',
            'bio': 'test'
        }
        genre_params = {
            'title': 'test',
            'description': 'test'
        }
        author = AuthorFactory.create(**author_params)
        genre = GenreFactory.create(**genre_params)
        book = BookFactory.create(**book_params, authors=[author], genres=[genre])
        books_url = reverse('books-detail', args=[book.id])
        
        resp = simplejson.loads(client.get(books_url).content)
        expected_resp = {
            'id': 1, 
            'title': 'test', 
            'page_count': 500, 
            'description': 'test_description', 
            'authors': [{'first_name': 'John', 'last_name': 'Dad', 'bio': 'test'}], 
            'genres': [{'title': 'test', 'description': 'test'}]
        }
        
        assert resp == expected_resp

    def test_not_owner_can_not_change_book(self, client):
        books_url = reverse('books-list')

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

        books_create_params = simplejson.dumps({
            'title': 'Lord of the rings'
        })

        UserFactory.create(**user_params_owner)
        UserFactory.create(**user_params_not_owner)

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        client.post(books_url, books_create_params, **token_dict_owner)

        created_book = Book.objects.get(title='Lord of the rings')
        books_detail = reverse('books-detail', args=[created_book.id])

        user_params_not_owner.pop('email')
        token_dict_not_owner = get_login_params_dict(client, user_params_not_owner)

        resp = simplejson.loads(
            client.put(
                books_detail, simplejson.dumps({'title': 'Hobbit'}), **token_dict_not_owner
            ).content
        )

        expected_resp = {'detail': 'You do not have permission to perform this action.'}

        assert resp == expected_resp

    def test_owner_can_change_book(self, client):
        books_url = reverse('books-list')

        user_params_owner = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'test'
        }

        books_create_params = simplejson.dumps({
            'title': 'Lord of the rings'
        })
        new_title = 'Hobbit'

        UserFactory.create(**user_params_owner)

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        client.post(books_url, books_create_params, **token_dict_owner)

        created_book = Book.objects.get(title='Lord of the rings')
        books_detail = reverse('books-detail', args=[created_book.id])

        token_dict_owner = get_login_params_dict(client, user_params_owner)

        resp = simplejson.loads(
            client.put(
                books_detail, simplejson.dumps({'title': new_title}), **token_dict_owner
            ).content
        )

        assert resp.get('title') == new_title
