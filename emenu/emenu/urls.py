from django.contrib import admin
from django.urls import include, path

api_urlpatterns = [
    path("", include("menus.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((api_urlpatterns, "api"), namespace="api")),
]
