from common.permissions import BaseIsOwnerOrReadOnly


class IsRegisteredUserOwnerOrReadonly(BaseIsOwnerOrReadOnly):
    """
    Custom permission Class to override _get_obj method
    """

    @staticmethod
    def _get_obj(obj):
        return obj
