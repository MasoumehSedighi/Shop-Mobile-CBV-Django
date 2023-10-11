from django.db import models
from pathlib import Path
from django.utils import timezone
import uuid
import os

# Create your models here.

def _get_product_image_upload_path(instance, file):
    path = Path( instance.category.name)
    path = path / timezone.now().strftime("%Y/%m/%d")
    new_name = str(uuid.uuid4())
    ext = os.path.splitext(file)[1]
    return path/ f"{new_name}{ext}"




class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    description = models.TextField()
    image = models.ImageField(upload_to =_get_product_image_upload_path, null=True, blank=True)
    count = models.PositiveBigIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.name