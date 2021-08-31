from django.db import models
from django_extensions.db.models import TimeStampedModel


class Menu(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} - MENU"


class Dish(TimeStampedModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dishes")
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)
    price = models.FloatField(default=0)
    photo = models.ImageField(
        upload_to="photos",
        max_length=255,
        blank=True,
        null=True,
    )
    prepare_time = models.IntegerField(default=30)  # minutes
    vegan = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} - {self.price} pln - DISH"
