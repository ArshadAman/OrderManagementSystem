from django.db import models
import uuid

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('RECEIVED', 'Received'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    )
    order_name = models.CharField(max_length=100)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RECEIVED')
    customer_email = models.EmailField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return f'{self.order_name} - {self.order_status}'