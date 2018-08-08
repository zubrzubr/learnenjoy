from rest_framework import serializers

from reward.serializers import RewardSerializer
from target.models import Target
from book.serializers import BookBaseSerializer
from target.services import ProgressService


class BaseTargetSerializer(serializers.ModelSerializer):
    """
    Serializer for target creation.
    """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    reward = RewardSerializer(many=False, required=False)
    pages_per_day = serializers.SerializerMethodField()

    class Meta:
        model = Target
        fields = (
            'title', 'description', 'book', 'current_page_progress', 'start_date', 'end_date', 'owner', 'reward',
            'pages_per_day',
        )

    def get_pages_per_day(self, obj):
        return ProgressService(obj).get_pages_daily_target()


class TargetSerializer(BaseTargetSerializer):
    """
    Serializer to present all targets.
    """
    book = BookBaseSerializer(many=False)
