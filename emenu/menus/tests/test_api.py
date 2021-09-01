from django.contrib.auth.models import User
from django.urls import reverse
from menus.tests.factories import DishFactory, MenuFactory
from rest_framework.test import APITestCase


class MenuTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.menu = MenuFactory()
        self.menu.save()
        self.menu2 = MenuFactory()
        self.menu2.save()
        self.menu3 = MenuFactory()
        self.menu3.save()
        self.dish = DishFactory(menu=self.menu)
        self.dish.save()
        self.dish2 = DishFactory(menu=self.menu)
        self.dish2.save()
        self.dish3 = DishFactory(menu=self.menu)
        self.dish3.save()
        self.dish4 = DishFactory(menu=self.menu)
        self.dish4.save()

    def test_get_non_null_menus_by_logged_user(self):
        url = reverse("api:menus-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0]["id"], self.menu.id)

    def test_post_menu_by_logged_user(self):
        url = reverse("api:menus-list")
        data = {"name": "Testowe menu", "description": "To jest moja pierwsza testowa karta menu :)"}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], data["name"])
        self.assertEqual(response.json()["description"], data["description"])

    def test_get_menu_details_by_logged_user(self):
        url = reverse("api:menus-detail", args=[self.menu.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], self.menu.id)
        self.assertEqual(response.json()["name"], self.menu.name)
        self.assertEqual(response.json()["description"], self.menu.description)
        self.assertIsNotNone(response.json()["dishes"])

    def test_put_menu_details_by_logged_user(self):
        url = reverse("api:menus-detail", args=[self.menu.id])
        data = {"name": "Testowe menu", "description": "To jest moja pierwsza testowa karta menu :)"}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], data["name"])
        self.assertEqual(response.json()["description"], data["description"])

    def test_delete_menu_details_by_logged_user(self):
        url = reverse("api:menus-detail", args=[self.menu.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

    def test_get_menu_without_dishes_details_by_logged_user(self):
        url = reverse("api:menus-detail", args=[self.menu2.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


class DishTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.menu = MenuFactory()
        self.menu.save()
        self.menu2 = MenuFactory()
        self.menu2.save()
        self.menu3 = MenuFactory()
        self.menu3.save()
        self.dish = DishFactory(menu=self.menu)
        self.dish.save()
        self.dish2 = DishFactory(menu=self.menu)
        self.dish2.save()
        self.dish3 = DishFactory(menu=self.menu)
        self.dish3.save()
        self.dish4 = DishFactory(menu=self.menu)
        self.dish4.save()

    def test_get_dish_by_logged_user(self):
        url = reverse("api:menu-dishes-list", args=[self.menu.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), 4)
