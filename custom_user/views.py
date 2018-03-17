from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from custom_user.models import CustomUser
from custom_user.serializers import BaseUserSerializer, CreateUserSerializer
from custom_user.permissions import IsRegisteredUserOrReadonly


class CustomUsersViewSet(viewsets.ModelViewSet):
    """
    Model view for targets, presents: detail view, and list view for targets.
    """
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny, IsRegisteredUserOrReadonly)
    http_method_names = ['get', 'post', 'head', 'put']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return BaseUserSerializer
