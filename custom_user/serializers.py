from rest_framework import serializers

from custom_user.models import CustomUser


class BaseUserSerializer(serializers.ModelSerializer):
    """
    Serializer to present users.
    """
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'bio', 'country', 'city', 'birth_date', 'favorite_books', 'targets'
        )


class CreateUserSerialzer(serializers.ModelSerializer):
    """
    Used for user's registration
    """
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'bio', 'country', 'city', 'email', 'username', 'password', 
            'birth_date', 'favorite_books', 'targets'
        )
   
    def create(self, validated_data):
        user = super(CreateUserSerialzer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
