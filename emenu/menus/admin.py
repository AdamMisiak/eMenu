from django.contrib import admin

from .models import Dish, Menu


class DishInline(admin.StackedInline):
    readonly_fields = ["modified", "created"]
    model = Dish
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created", "modified")
    search_fields = ("name", "description")
    ordering = ("name",)
    readonly_fields = ["modified", "created"]

    inlines = [DishInline]


admin.site.register(Menu, MenuAdmin)
