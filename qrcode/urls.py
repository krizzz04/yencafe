from django.urls import path
from . import views

urlpatterns = [
    path('generate/<int:order_id>/', views.GenerateQRCode.as_view(), name='generate-qr'),  # POST /api/qr/generate/1/
    path('verify/<str:code>/', views.VerifyQRCode.as_view(), name='verify-qr'),  # GET /api/qr/verify/abc123/
] 