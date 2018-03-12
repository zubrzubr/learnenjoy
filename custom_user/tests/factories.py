import datetime

import factory.fuzzy
from django.contrib.auth.models import Group

from custom_user.models import CustomUser


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

    @factory.post_generation
    def targets(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for target in extracted:
                self.targets.add(target)

    @factory.post_generation
    def favorites_books(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for book in extracted:
                self.favorites_books.add(book)
