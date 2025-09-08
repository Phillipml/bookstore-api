import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from order.models import Order
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory, CategoryFactory


class TestOrderViewSet(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.product = ProductFactory()
        self.category = CategoryFactory()
        self.product.category.add(self.category)

    def test_order(self):
        order = OrderFactory()
        order.product.add(self.product)

        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)[0]
        self.assertEqual(order_data["product"][0]["title"], self.product.title)
        self.assertEqual(order_data["product"][0]["price"], self.product.price)
        self.assertEqual(order_data["product"][0]["active"], self.product.active)
        self.assertEqual(
            order_data["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"product_id": [product.id], "user": user.id})

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)
