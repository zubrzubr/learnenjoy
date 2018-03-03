from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from target.models import Target
from target.serializers import TargetSerializer, BaseTargetSerializer
from common.permissions import BaseIsOwnerOrReadOnly


class TargetsViewSet(viewsets.ModelViewSet):
    """
    Model view for targets, presents: detail view, and list view for targets.
    """
    queryset = Target.objects.all()
    permission_classes = (BaseIsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_serializer_class(self):
        if self.action == 'create':
            return BaseTargetSerializer
        return TargetSerializer
