from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reward.models import Reward
from reward.serializers import RewardSerializer
from common.permissions import BaseIsOwnerOrReadOnly


class RewardsViewSet(viewsets.ModelViewSet):
    """
    Model view for Rewards, presents: detail view, and list view for rewards.
    """
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = (BaseIsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
