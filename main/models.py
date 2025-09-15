from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('footwear', 'Footwear'),
        ('equipment', 'Equipment'),
        ('accessories', 'Accessories'),
        ('merchandise', 'Merchandise'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()   #gambar item
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False) #status unggulan item