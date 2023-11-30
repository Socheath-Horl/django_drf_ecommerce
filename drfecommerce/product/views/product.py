from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from drfecommerce.product.models import Product
from drfecommerce.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all products
    """

    queryset = Product.objects.all()
    lookup_field = 'slug'

    def retrieve(self, request: Request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def list(self, request: Request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path=r'category/(?P<category>\w+)/all',)
    def list_product_by_category(self, request: Request, category=None):
        """"
        An endpoint to return products by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
