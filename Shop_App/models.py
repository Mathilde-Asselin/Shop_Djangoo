from operator import mod
from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=30)
    img = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    

