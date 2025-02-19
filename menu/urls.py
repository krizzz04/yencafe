from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuItemList.as_view(), name='menu-list'),
]