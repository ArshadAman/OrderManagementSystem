from django.db import models
import uuid
from datetime import date

class Order(models.Model):
    STATUS_CHOICES = (
        ('RECEIVED', 'Received'),
        ('PROCESSING', 'Processing'),
        ('CUTTING', 'Cutting'),
        ('STICHING', 'Stiching'),
        ('DELIVERED', 'Delivered'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    order_name = models.CharField(max_length=100, blank=False)
    order_quantity = models.IntegerField(default=1, blank=False)
    customer_email = models.EmailField(max_length=300, null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=False)
    order_recieved_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    order_due_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    order_priorty = models.IntegerField(default=0, blank=True, null=True)
    order_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='RECEIVED')

    def __str__(self) -> str:
        return f"{self.customer_name}'s order of - {self.order_name} has been {self.order_status}"
    
    def save(self,*args, **kwargs):
        if self.order_due_date:
            days_remaining = (self.order_due_date - date.today()).days
            self.order_priorty = max(0, days_remaining)
        super().save(*args, **kwargs)


class Mesurement(models.Model):

    SLITS_CHOICES = (
        (None, 'None'),
        ('Side', 'Side'),
        ('Center', 'Center'),
    )
    Rise = (
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    )
    Pleat = (
        ("Flat Front", "Flat Front"),
        ("1 Pleat", "1 Pleat"),
        ("2 Pleat", "2 Pleat"),
    )
    Belt = (
        ("Cut Belt", "Cut Belt"),
        ("Ext. Belt", "Ext. Belt"),
    )

    Pockets = (
        ("Cross", "Cross"),
        ("Side", "Side"),
    )
    WatchPockets = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    WatchPockets_Number = (
        (1, 1),
        (2, 2),
    )
    MobilePockets = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    CUT = (
        ("Slim 4'", "Slim 4'"),
        ("M FIT 5'", "M FIT 5'"),
        ("Loose 6'", "Loose 6'"),
    )
    STYLE = (
        ("Square Slit", "Square Slit"),
        ("Open Shirt", "M FIT 5'"),
    )
    Neck = (
        ("Regular", "Regular"),
        ("Short", "Short"),
        ("Long", "Long"),
    )
    CollorPoint = (
        (2, 2),
        (2.5, 2.5),
        (2.75, 2.75),
    )
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, default=uuid.uuid4, related_name='measurement', blank=True)
    customer_name = models.CharField(max_length=100, blank=False, null=True)
    customer_email = models.EmailField(max_length=300, blank=False, null=True)
    customer_phone = models.IntegerField(blank=False, null=False)

    # Blazer and Jacket 

    front_length = models.CharField(max_length=20, blank=True, null=True)
    shoulder = models.CharField(max_length=20, blank=True, null=True)
    sleeves = models.CharField(max_length=20, blank=True, null=True)
    chest = models.CharField(max_length=20, blank=True, null=True)
    waist = models.CharField(max_length=20, blank=True, null=True)
    hip = models.CharField(max_length=20, blank=True, null=True)
    crossfront = models.CharField(max_length=20, blank=True, null=True)
    crossback = models.CharField(max_length=20, blank=True, null=True)
    sherwani_vest = models.CharField(max_length=50, blank=True, null=True)
    slits = models.CharField(
        max_length=10, choices=SLITS_CHOICES, null=True, blank=True)
    
    Blazer_Jacket_Additional_Information = models.TextField(max_length=2000, blank=True, null=True)
    Blazer_sample_cloth_image = models.ImageField(upload_to="sample_images/blazers", blank=True, null=True)
    

    # Kurta Mesurement

    kurta_front_length = models.CharField(max_length=20, blank=True, null=True)
    kurta_shoulder = models.CharField(max_length=20, blank=True, null=True)
    kurta_sleeves = models.CharField(max_length=20, blank=True, null=True)
    kurta_chest = models.CharField(max_length=20, blank=True, null=True)
    kurta_waist = models.CharField(max_length=20, blank=True, null=True)
    kurta_hip = models.CharField(max_length=20, blank=True, null=True)
    kurta_sleeves_opening = models.CharField(
        max_length=20, blank=True, null=True)
    kurta_biceps = models.CharField(max_length=20, blank=True, null=True)

    kurta_Cut_Choices = models.CharField(
        max_length=20, choices=CUT, blank=True, null=True)
    kurta_Style_Choices = models.CharField(
        max_length=20, choices=STYLE, blank=True, null=True)
    kurta_Neck_Choices = models.CharField(
        max_length=20, choices=Neck, blank=True, null=True)
    kurta_Collor_Choices = models.FloatField(
        max_length=20, choices=CollorPoint, blank=True, null=True)
    
    Kurta_Shirt_Additional_Information = models.TextField(max_length=2000, blank=True, null=True)
    Kurta_sample_cloth_image = models.ImageField(upload_to="sample_images/kurta", blank=True, null=True)

    # Trouser Mesurement

    Tourser_length = models.CharField(max_length=20, blank=True, null=True)
    Tourser_inseam = models.CharField(max_length=20, blank=True, null=True)
    Tourser_bottom = models.CharField(max_length=20, blank=True, null=True)
    Tourser_knee = models.CharField(max_length=20, blank=True, null=True)
    Tourser_thigh = models.CharField(max_length=20, blank=True, null=True)
    Tourser_waist = models.CharField(max_length=20, blank=True, null=True)
    Tourser_hips = models.CharField(max_length=20, blank=True, null=True)
    Tourser_rounding = models.CharField(max_length=20, blank=True, null=True)

    Rise_Choices = models.CharField(
        max_length=20, choices=Rise, blank=True, null=True)
    front_Down = models.CharField(max_length=50, blank=True, null=True)

    Pleat_Choices = models.CharField(
        max_length=20, choices=Pleat, blank=True, null=True)
    Belt_Choices = models.CharField(
        max_length=20, choices=Belt, blank=True, null=True)
    Pocket_Choices = models.CharField(
        max_length=20, choices=Pockets, blank=True, null=True)
    Watch_Pocket_Choices = models.CharField(
        max_length=20, choices=WatchPockets, blank=True, null=True)
    Watch_Pocket_Number = models.IntegerField(
        choices=WatchPockets_Number, blank=True, null=True)
    Mobile_Pockets = models.CharField(
        max_length=20, choices=MobilePockets, blank=True, null=True)
    pocketSize = models.CharField(max_length=50, blank=True, null=True)

    Trouser_Additional_Information = models.TextField(max_length=2000, blank=True, null=True)
    Trouser_sample_cloth_image = models.ImageField(upload_to="sample_images/trouser", blank=True, null=True)

    # Images 
    blazer_image = models.ImageField(upload_to='blazer_images', blank=True, null=True, default='/form/blazer-jacket.bmp')
    kurta_image = models.ImageField(upload_to='kurta_images', blank=True, null=True, default='/form/shirt-kurta.bmp')
    trouser_image = models.ImageField(upload_to='trouser_images', blank=True, null=True, default='/form/trouser.bmp')

    def __str__(self) -> str:
        return f"{self.customer_name}'s - Mesurement"
