import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from product.models import Category
from product.factories import CategoryFactory


class CategoryViewSet(TestCase):
    def setUp(self):
        self.category = CategoryFactory()

    def test_create_category(self):
        data = json.dumps({"title": "terror", "description": "categoria de terror"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_category = Category.objects.get(id=response.data["id"])
        self.assertEqual(created_category.title, "terror")

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)
        self.assertEqual(category_data[0]["title"], self.category.title)
