from django.shortcuts import render
from rest_framework import generics, permissions
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return MenuItem.objects.filter(is_available=True)

class MenuItemDetail(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
