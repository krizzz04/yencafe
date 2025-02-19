from rest_framework import serializers
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category', 'category_name', 'image', 'is_available'] 