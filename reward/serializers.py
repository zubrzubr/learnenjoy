from rest_framework import serializers

from reward.models import Reward


class RewardSerializer(serializers.ModelSerializer):
    """
    Main reward's serializer
    """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reward
        fields = ('id', 'name', 'url', 'owner')
