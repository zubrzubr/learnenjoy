from rest_framework import viewsets

from custom_user.models import CustomUser
from custom_user.serializers import UserSerializer


class CustomUsersViewSet(viewsets.ModelViewSet):
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
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
