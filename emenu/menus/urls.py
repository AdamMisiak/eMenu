from django.urls import include, path
from rest_framework import routers

from .viewsets import MenuViewset

router = routers.SimpleRouter()
router.register(r"menus", MenuViewset, "menus")

urlpatterns = [
    path("", include(router.urls)),
]
