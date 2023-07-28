from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from parser.models import Product


class ProductSerializer(ModelSerializer):
    """Serializer for model Product"""

    class Meta:
        model = Product
        fields = '__all__'


class ParserSerializer(Serializer):
    products_count = serializers.IntegerField(default=10, min_value=1, max_value=50)
