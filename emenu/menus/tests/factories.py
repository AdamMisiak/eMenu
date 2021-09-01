import factory
from factory import fuzzy
from faker import Faker
from menus.models import Dish, Menu

faker = Faker(["pl_PL"])


class MenuFactory(factory.Factory):
    class Meta:
        model = Menu

    name = factory.LazyFunction(lambda: faker.text(max_nb_chars=50))
    description = factory.LazyFunction(lambda: faker.text(max_nb_chars=100))


class DishFactory(factory.Factory):
    class Meta:
        model = Dish

    name = factory.LazyFunction(lambda: faker.text(max_nb_chars=50))
    description = factory.LazyFunction(lambda: faker.text(max_nb_chars=100))
    price = fuzzy.FuzzyInteger(5, 200)
    photo = factory.django.FileField(filename="test.jpg")
    prepare_time = fuzzy.FuzzyInteger(5, 60)
    vegan = faker.pybool()
