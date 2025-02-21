from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'menu_item_name', 'quantity', 'price',]
        read_only_fields = ['price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'special_instructions', 'total_amount', 'table_number', 'items']  # Add table_number here
        read_only_fields = ['user', 'created_at', 'total_amount', 'status']