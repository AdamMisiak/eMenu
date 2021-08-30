from django.db import models
from django_extensions.db.models import TimeStampedModel


class Menu(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000, blank=True, null=True)


class Dish(TimeStampedModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dishes", blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField(blank=True, default=0)
    photo = models.ImageField(
        upload_to="photos",
        max_length=255,
    )
    prepare_time = models.IntegerField(blank=True, default=30)  # minutes
    vegan = models.BooleanField(default=False)