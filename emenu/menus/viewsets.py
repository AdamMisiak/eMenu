from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter

from .filters import MenuFilter
from .models import Dish, Menu
from .serializers import (
    DishCreateSerializer,
    DishSerializer,
    MenuCreateSerializer,
    MenuDetailsSerializer,
    MenuSerializer,
)


class MenuViewset(viewsets.ModelViewSet):
    """
    Lists/creates/updates/deletes menus.
    """

    serializer_class = MenuSerializer
    queryset = Menu.objects.all().annotate(dish_count=Count("dishes"))
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = MenuFilter
    ordering_fields = ("name", "dish_count")

    def get_serializer_class(self):
        if self.action in ["list"]:
            return MenuSerializer
        if self.action in ["retrieve"]:
            return MenuDetailsSerializer
        elif self.action in ["create", "update", "partial update"]:
            return MenuCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(dishes__isnull=False).distinct()

    @method_decorator(cache_page(60 * 15))
    def list(self, request, **kwargs):
        return super().list(request, **kwargs)


class DishViewset(viewsets.ModelViewSet):
    """
    Lists/creates/updates/deletes dishes.
    """

    serializer_class = DishSerializer
    queryset = Dish.objects.all().order_by("name")
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return DishSerializer
        elif self.action in ["create", "update", "partial update"]:
            return DishCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(menu=self.kwargs["menus_pk"]).distinct()

    @method_decorator(cache_page(60 * 15))
    def list(self, request, **kwargs):
        return super().list(request, **kwargs)
