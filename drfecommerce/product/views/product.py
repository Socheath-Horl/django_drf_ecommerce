from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from drfecommerce.product.models import Product
from drfecommerce.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request: Request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
