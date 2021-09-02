from django.db.models import Count
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

    Only for authenticated users.
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
        from django.core.mail import get_connection, send_mail

        conn = get_connection(backend="django.core.mail.backends.dummy.EmailBackend")
        send_mail(
            subject="subject",
            message="message",
            from_email="emenu@emenu.dev",
            recipient_list=[
                "adammisiak3@gmail.com",
            ],
            fail_silently=False,
            connection=conn,
        )
        return self.queryset.filter(dishes__isnull=False).distinct()


class DishViewset(viewsets.ModelViewSet):
    """
    Lists/creates/updates/deletes dishes.

    Only for authenticated users.
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
