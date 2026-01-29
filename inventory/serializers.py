from rest_framework import serializers
from catalog.models import Product
from .models import Inventory


class ProductNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')

class InventorySerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.all(),
        write_only=True
    )

    class Meta:
        model = Inventory
        fields = '__all__'
