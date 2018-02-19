from rest_framework import serializers

from custom_user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to present users. Response example:
    [
        {
            "first_name": "User name",
            "last_name": "Last name",
            "bio": "Test bio",
            "country": "Ukraine",
            "city": "Kyiv",
            "birth_date": "1991-11-11",
            "favorite_books": [],
            "targets": 1
        }
    ]
    """
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'bio', 'country', 'city', 'birth_date', 'favorite_books', 'targets')
