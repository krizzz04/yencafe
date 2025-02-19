from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # API endpoints - remove the 'api/' prefix since it's in the root urls.py
    path('orders/<int:pk>/update-status/', views.update_order_status, name='update-order-status'),
    path('orders/<int:pk>/', views.OrderAPIDetail.as_view(), name='order-api-detail'),
    path('orders/', views.OrderAPIList.as_view(), name='order-api-list'),
    
    # Regular views
    path('web/orders/', views.OrderList.as_view(), name='order-list'),
    path('web/staff/dashboard/', views.StaffDashboardView.as_view(), name='staff-dashboard'),
]