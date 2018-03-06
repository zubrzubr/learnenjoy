from rest_framework import serializers

from reward.models import Reward


class RewardSerializer(serializers.ModelSerializer):
    """
    Main reward's serializer
    """
    class Meta:
        model = Reward
        fields = ('id', 'name', 'url')
