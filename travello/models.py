from django.db import models

# Create your models here.

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    desc = models.TextField()
    price = models.ImageField()
    offer = models.BooleanField(default=False)