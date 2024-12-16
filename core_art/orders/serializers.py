from rest_framework import serializers
from .models import Cart, CartItem, Order

# Cart Iteam Serializer
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'cart']

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

# Cart Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'buyer', 'seller', 'product', 'quantity', 'total_price', 'admin_commission', 'seller_earnings', 'created_at']
