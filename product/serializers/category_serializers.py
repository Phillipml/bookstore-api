from rest_framework import serializers
from django.utils.text import slugify

from product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        if "slug" not in validated_data or not validated_data["slug"]:
            validated_data["slug"] = slugify(validated_data["title"])
        return super().create(validated_data)
