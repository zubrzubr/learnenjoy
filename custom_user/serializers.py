from rest_framework import serializers

from custom_user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to present users.
    """
    password = serializers.CharField(write_only=True)
 
    class Meta:
            model = CustomUser
            fields = (
                'first_name', 'last_name', 'email', 'username', 'password', 'bio', 'country', 'city',
                'birth_date', 'favorite_books', 'targets'
            )

    def create(self, validated_data):
        user=super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
