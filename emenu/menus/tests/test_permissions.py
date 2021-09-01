from django.contrib.auth.models import User
from django.urls import reverse
from menus.tests.factories import DishFactory, MenuFactory
from rest_framework.test import APITestCase


class MenuTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.menu = MenuFactory()
        self.menu.save()
        self.dish = DishFactory(menu=self.menu)
        self.dish.save()
        self.dish2 = DishFactory(menu=self.menu)
        self.dish2.save()

    def test_get_non_null_menus_by_anon_user(self):
        url = reverse("api:menus-list")
        self.client.logout()
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
