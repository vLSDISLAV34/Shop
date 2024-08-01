from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=75)
    price = models.FloatField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)