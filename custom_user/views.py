from rest_framework import viewsets

from custom_user.models import CustomUser
from custom_user.serializers import BaseUserSerializer, CreateUserSerializer
from custom_user.permissions import IsRegisteredUserOwnerOrReadonly


class CustomUsersViewSet(viewsets.ModelViewSet):
    """
    Model view for targets, presents: detail view, and list view for targets.
    """
    queryset = CustomUser.objects.filter(is_superuser=False)
    permission_classes = (IsRegisteredUserOwnerOrReadonly,)
    http_method_names = ['get', 'post', 'head', 'put']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return BaseUserSerializer
