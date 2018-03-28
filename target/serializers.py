from rest_framework import serializers

from target.models import Target
from book.serializers import BookBaseSerializer


class BaseTargetSerializer(serializers.ModelSerializer):
    """
    Serializer for target creation.
    """
    class Meta:
        model = Target
        fields = ('title', 'description', 'book', 'current_page_progress', 'start_date', 'end_date')


class TargetSerializer(BaseTargetSerializer):
    """
    Serializer to present all targets.
    """
    book = BookBaseSerializer(many=False)
