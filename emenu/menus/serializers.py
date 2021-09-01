from rest_framework import serializers
from utils.serializers import CurrentUrlObject

from .models import Dish, Menu


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "description",
            "price",
            "photo",
            "prepare_time",
            "vegan",
        )


class DishCreateSerializer(serializers.ModelSerializer):
    menu = serializers.HiddenField(default=CurrentUrlObject(Menu, "menus_pk"))

    class Meta:
        model = Dish
        fields = (
            "menu",
            "name",
            "description",
            "price",
            "photo",
            "prepare_time",
            "vegan",
        )


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = (
            "id",
            "name",
            "description",
            "dishes",
        )
        read_only_fields = fields


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            "name",
            "description",
        )
