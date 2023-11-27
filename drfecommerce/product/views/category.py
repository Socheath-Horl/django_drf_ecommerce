from models import Category
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from serializers import CategorySerializer


class CategoryView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all categories
    """

    queryset = Category.objects.all()

    def list(self, request: Request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
