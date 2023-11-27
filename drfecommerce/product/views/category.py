from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from drfecommerce.product.models import Category
from drfecommerce.product.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request: Request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
