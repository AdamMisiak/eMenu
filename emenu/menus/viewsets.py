from django.db.models import Count
from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter

from .filters import MenuFilter
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
    queryset = Menu.objects.all().annotate(dish_count=Count("dishes"))
    permission_classes = (MenuPermission,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = MenuFilter
    ordering_fields = ("name", "dish_count")

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return MenuSerializer
        elif self.action in ["create", "update", "partial update"]:
            return MenuCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(dishes__isnull=False).distinct()


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
