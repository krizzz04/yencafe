from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
import qrcode
from io import BytesIO
import base64
from .models import QRCode
from .serializers import QRCodeSerializer

# Create your views here.

class GenerateQRCode(generics.CreateAPIView):
    serializer_class = QRCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f'Order:{order_id}')
        qr.make(fit=True)
        
        # Create QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return Response({'qr_code': img_str}, status=status.HTTP_201_CREATED)

class VerifyQRCode(generics.RetrieveAPIView):
    serializer_class = QRCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'

    def get_queryset(self):
        return QRCode.objects.filter(is_valid=True)
