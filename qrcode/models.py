from django.db import models
from orders.models import Order

# Create your models here.

class QRCode(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
