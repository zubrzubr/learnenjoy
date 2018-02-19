from rest_framework import viewsets

from target.models import Target
from target.serializers import TargetSerializer


class TargetsViewSet(viewsets.ModelViewSet):
    """
    Model view for targets, presents:
        detail view, and list view for targets.
    Response example:
    [
        {
            "title": "Test",
            "description": "test",
            "book": {
                "id": 1,
                "title": "Test",
                "description": "Test",
                "authors": [
                    {
                        "first_name": "test",
                        "last_name": "test",
                        "bio": "test"
                    }
                ],
                "genre": {
                    "title": "test",
                    "description": "test"
                }
            },
            "start_date": "2018-02-19",
            "end_date": "2018-02-22"
        }
    ]
    """
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
