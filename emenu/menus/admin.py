from django.contrib import admin

from .models import Dish, Menu


class DishInline(admin.StackedInline):
    model = Dish
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)

    inlines = [DishInline]


admin.site.register(Menu, MenuAdmin)
