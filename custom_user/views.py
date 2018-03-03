from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from custom_user.models import CustomUser
from custom_user.serializers import UserSerializer


class CustomUsersViewSet(viewsets.ModelViewSet):
    """
    Model view for targets, presents: detail view, and list view for targets.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
