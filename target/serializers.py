from rest_framework import serializers

from reward.serializers import RewardSerializer
from target.models import Target
from book.serializers import BookBaseSerializer


class BaseTargetSerializer(serializers.ModelSerializer):
    """
    Serializer for target creation.
    """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    reward = RewardSerializer(many=False, required=False)

    class Meta:
        model = Target
        fields = ('title', 'description', 'book', 'current_page_progress', 'start_date', 'end_date', 'owner', 'reward')


class TargetSerializer(BaseTargetSerializer):
    """
    Serializer to present all targets.
    """
    book = BookBaseSerializer(many=False)
