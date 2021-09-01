from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now, timedelta
from menus.tests.factories import DishFactory, MenuFactory
from rest_framework.test import APITestCase


class MenuTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.menu = MenuFactory(name="Menu letnie")
        self.menu.save()
        self.menu2 = MenuFactory(name="Promocyjne menu letnie")
        self.menu2.save()
        self.menu3 = MenuFactory(name="Menu zimowa karta")
        self.menu3.save()
        self.menu4 = MenuFactory(name="Jesienna promocja")
        self.menu4.save()
        self.dish = DishFactory(menu=self.menu, name="Schabowy")
        self.dish.save()
        self.dish2 = DishFactory(menu=self.menu2, name="Pizza")
        self.dish2.save()
        self.dish3 = DishFactory(menu=self.menu3, name="Pepsi")
        self.dish3.save()
        self.dish4 = DishFactory(menu=self.menu3, name="Barszcz")
        self.dish4.save()
        self.dish5 = DishFactory(menu=self.menu3, name="Piwo Perla")
        self.dish5.save()
        self.dish6 = DishFactory(menu=self.menu, name="Salatka")
        self.dish6.save()

        self.yesterday = (now() - timedelta(days=1)).strftime("%Y-%m-%d")
        self.today = now().strftime("%Y-%m-%d")
        self.tomorrow = (now() + timedelta(days=1)).strftime("%Y-%m-%d")

    def test_get_filtered_by_name_menus(self):
        url = reverse("api:menus-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, {"name": "me"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), 3)

        response = self.client.get(url, {"name": "pudlo"})
        self.assertEqual(len(response.json()["results"]), 0)

        response = self.client.get(url, {"name": "promo"})
        self.assertEqual(len(response.json()["results"]), 1)

    def test_get_filtered_by_created_and_modified_menus(self):
        url = reverse("api:menus-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, {"created_to": self.tomorrow})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), 3)

        response = self.client.get(url, {"created_to": self.tomorrow, "created_from": self.today})
        self.assertEqual(len(response.json()["results"]), 3)

        response = self.client.get(url, {"modified_to": self.yesterday})
        self.assertEqual(len(response.json()["results"]), 0)

        response = self.client.get(url, {"created_to": self.tomorrow, "name": "letni"})
        self.assertEqual(len(response.json()["results"]), 2)

        response = self.client.get(url, {"modified_from": self.yesterday, "name": "test"})
        self.assertEqual(len(response.json()["results"]), 0)

    def test_get_ordered_by_name_menus(self):
        url = reverse("api:menus-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, {"ordering": "name"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["results"]), 3)
        self.assertEqual(response.json()["results"][0]["id"], self.menu.id)
        self.assertEqual(response.json()["results"][1]["id"], self.menu3.id)
        self.assertEqual(response.json()["results"][2]["id"], self.menu2.id)

        response = self.client.get(url, {"ordering": "-dish_count"})
        self.assertEqual(len(response.json()["results"]), 3)
        self.assertEqual(response.json()["results"][0]["id"], self.menu3.id)
        self.assertEqual(response.json()["results"][1]["id"], self.menu.id)
        self.assertEqual(response.json()["results"][2]["id"], self.menu2.id)
