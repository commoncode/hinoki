from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    english_name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.CharField(max_length=250)
    item_number = models.IntegerField()
    is_vegetarian = models.BooleanField()
    is_vegan = models.BooleanField()
    is_glutenfree = models.BooleanField()
