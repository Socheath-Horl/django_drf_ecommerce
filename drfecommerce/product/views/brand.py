from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from drfecommerce.product.models import Brand
from drfecommerce.product.serializers import BrandSerializer


class BrandViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request: Request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
