from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from parser.models import Product
from parser.serializers import ProductSerializer


class ListProductsView(ListCreateAPIView):
    """Class for viewing list of products or starting parsing ozon"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        elif self.request.method == 'POST':
            return ProductSerializer


class DetailProductsView(RetrieveAPIView):
    """Class for viewing detail product """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()