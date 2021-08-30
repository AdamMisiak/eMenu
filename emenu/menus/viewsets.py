from rest_framework import permissions, viewsets

from .models import Menu
from .serializers import MenuSerializer


class MenuViewset(viewsets.ModelViewSet):
    """
    Lists/creates/updates/deletes menus.

    Only for authenticated users.
    """

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
