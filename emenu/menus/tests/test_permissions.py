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

    def test_get_menu_details_by_anon_user(self):
        url = reverse("api:menus-detail", args=[self.menu.id])
        self.client.logout()
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_post_menu_by_anon_user(self):
        url = reverse("api:menus-list")
        data = {"name": "Testowe menu", "description": "To jest moja pierwsza testowa karta menu :)"}
        self.client.logout()
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 403)
