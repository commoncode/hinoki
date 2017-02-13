from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    english_name = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.CharField(max_length=250, blank=True)
    item_number = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_glutenfree = models.BooleanField(default=False)

    def __str__(self):
         return str(self.item_number) + "-" + self.name
