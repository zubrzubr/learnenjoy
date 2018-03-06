import factory

from reward.models import Reward


class RewardFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'name_%d' % n)
    url = factory.Sequence(lambda n: 'http://www.test_%d.com' % n)

    class Meta:
        model = Reward
