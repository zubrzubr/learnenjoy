import datetime

import factory.fuzzy
from django.contrib.auth.models import Group

from custom_user.models import CustomUser
from book.tests.factories import BookFactory
from target.tests.factories import TargetFactory


class GroupFactory(factory.django.DjangoModelFactory):
    name = 'test_group'

    class Meta:
        model = Group


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_%d' % n)
    email = factory.Sequence(lambda n: 'email_%d@test.com' % n)
    bio = factory.fuzzy.FuzzyText(length=100)
    country = factory.Sequence(lambda n: 'test country %d' % n)
    city = factory.Sequence(lambda n: 'test city %d' % n)
    birth_date = factory.LazyFunction(datetime.datetime.utcnow)

    class Meta:
        model = CustomUser


class UserFactoryWithBooksAndTargets(UserFactory):
    favorites_books = factory.RelatedFactory(BookFactory, 'book')
    targets = factory.RelatedFactory(TargetFactory, 'target')

