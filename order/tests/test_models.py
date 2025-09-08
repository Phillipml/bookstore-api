import pytest
from django.contrib.auth.models import User
from order.models import Order
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory


class TestOrderModel:

    def test_order_creation(self):

        order = OrderFactory()
        assert order.user is not None
        assert order.pk is not None

    def test_order_with_products(self):

        products = ProductFactory.create_batch(3)
        order = OrderFactory()
        order.product.set(products)
        assert order.product.count() == 3

    def test_order_user_relationship(self):
        user = UserFactory()
        order = OrderFactory(user=user)
        assert order.user == user
