from django.db import models

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

    def __str__(self) -> str:
        return f'{self.order_name} - {self.order_status}'