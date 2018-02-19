from rest_framework import serializers

from target.models import Target
from book.serializers import BookBaseSerializer


class TargetSerializer(serializers.ModelSerializer):
    """
    Serializer to present all targets.
    """
    book = BookBaseSerializer(read_only=True, many=False)

    class Meta:
        model = Target
        fields = ('title', 'description', 'book', 'start_date', 'end_date')
