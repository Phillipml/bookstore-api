import json
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from order.models import Order
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory, CategoryFactory


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.product = ProductFactory()
        self.category = CategoryFactory()
        self.product.category.add(self.category)

    def test_order(self):

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        order = OrderFactory(user=self.user)
        order.product.add(self.product)

        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)

        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        product = ProductFactory()
        data = json.dumps({"product_id": [product.id], "user": self.user.id})

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=self.user)
        self.assertEqual(created_order.user, self.user)
