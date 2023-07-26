from rest_framework.serializers import ModelSerializer
from parser.models import Product


class ProductSerializer(ModelSerializer):
    """Serializer for model Product"""

    class Meta:
        model = Product
        fields = '__all__'

