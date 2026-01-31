from rest_framework import serializers
from catalog.models import Product
from .models import Inventory


class ProductNestedSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    brand_id = serializers.IntegerField(source='brand.id', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand_id', 'brand_name')

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
