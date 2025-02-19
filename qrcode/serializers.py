from rest_framework import serializers
from .models import QRCode

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'order', 'code', 'created_at', 'is_valid']
        read_only_fields = ['code', 'created_at'] 