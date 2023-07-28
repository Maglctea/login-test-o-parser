from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from parser.models import Product
from parser.serializers import ProductSerializer, ParserSerializer
from parser.tasks import parsing_start


class ListProductsView(ListCreateAPIView):
    """Class for viewing list of products or starting parsing ozon"""

    serializer_class = ParserSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        elif self.request.method == 'POST':
            return ParserSerializer

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            parsing_start.delay(serializer.data.get('products_count'))

        return Response(status=status.HTTP_200_OK)


class DetailProductsView(RetrieveAPIView):
    """Class for viewing detail product """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()