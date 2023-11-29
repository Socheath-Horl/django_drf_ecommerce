from rest_framework import serializers

from drfecommerce.product.models import ProductLine
from drfecommerce.product.serializers import ProductSerializer


class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductLine
        fields = "__all__"
