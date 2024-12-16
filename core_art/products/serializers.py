from rest_framework import serializers
from .models import Product, Category, Tag, ProductImage

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']

# Tag serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# Product images serializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'images', 'category', 'tags', 'created_at']
        read_only_fields = ['id', 'created_at']
