import random

from django.core.management.base import BaseCommand
from faker import Faker
from menus.tests.factories import DishFactory, MenuFactory

faker = Faker(["pl_PL"])


class Command(BaseCommand):
    help = "Generate X random menus"

    def add_arguments(self, parser):
        parser.add_argument("number", nargs="+", type=int)

    def handle(self, *args, **options):
        for i in range(options["number"][0]):
            menu = MenuFactory()
            menu.save()
            for j in range(random.randint(0, 8)):
                dish = DishFactory(menu=menu, vegan=faker.boolean(chance_of_getting_true=50))
                dish.save()
