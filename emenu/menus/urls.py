from django.urls import include, path
from rest_framework_nested import routers

from .viewsets import DishViewset, MenuViewset

router = routers.SimpleRouter()
router.register(r"menus", MenuViewset, "menus")

dishes_router = routers.NestedSimpleRouter(router, "menus", lookup="menus")
dishes_router.register("dishes", DishViewset, basename="menu-dishes")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(dishes_router.urls)),
]
