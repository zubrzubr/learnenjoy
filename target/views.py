from rest_framework import viewsets

from target.models import Target
from target.serializers import TargetSerializer
from common.permissions import BaseIsOwnerOrReadOnly


class TargetsViewSet(viewsets.ModelViewSet):
    """
    Model view for targets, presents: detail view, and list view for targets.
    """
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = (BaseIsOwnerOrReadOnly, )
