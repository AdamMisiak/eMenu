from rest_framework import permissions, viewsets

from .models import Dish, Menu
from .permissions import MenuPermission
from .serializers import (
    DishCreateSerializer,
    DishSerializer,
    MenuCreateSerializer,
    MenuSerializer,
)


class MenuViewset(viewsets.ModelViewSet):
    """
    Lists/creates/updates/deletes menus.

    Only for authenticated users.
    """

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = (MenuPermission,)

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return MenuSerializer
        elif self.action in ["create", "update", "partial update"]:
            return MenuCreateSerializer
        return self.serializer_class


class DishViewset(viewsets.ModelViewSet):
    """
    Lists/creates/updates/deletes dishes.

    Only for authenticated users.
    """

    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return DishSerializer
        elif self.action in ["create", "update", "partial update"]:
            return DishCreateSerializer
        return self.serializer_class
