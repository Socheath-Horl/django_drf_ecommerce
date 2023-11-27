from rest_framework import serializers

from drfecommerce.product.models import Product
from drfecommerce.product.serializers import (BrandSerializer,
                                              CategorySerializer)


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"
