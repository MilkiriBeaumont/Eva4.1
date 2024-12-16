# api/serializers.py
from rest_framework import serializers
from .models import User, Product, Order, ProductsOrders

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProductsOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsOrders
        fields = '__all__'