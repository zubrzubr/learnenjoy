import datetime

import factory.fuzzy

from target.models import Target
from book.tests.factories import BookFactory
from reward.tests.factories import RewardFactory


class TargetFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'title_%d' % n)
    description = factory.fuzzy.FuzzyText(length=100)
    book = factory.SubFactory(BookFactory)
    reward = factory.SubFactory(RewardFactory)
    start_date = factory.fuzzy.FuzzyNaiveDateTime(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 2, 1))
    end_date = factory.fuzzy.FuzzyNaiveDateTime(datetime.datetime(2019, 1, 1), datetime.datetime(2019, 2, 1))

    class Meta:
        model = Target
