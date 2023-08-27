from django.db import models

<<<<<<< HEAD
from product.models.category import Category

class Product(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500, blank=True, null=True)
  price = models.PositiveIntegerField(null=True)
  active = models.BooleanField(default=True)
  category = models.ManyToManyField(Category, blank=True)
=======
from product.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)


    def __str__(self):
        return self.title
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
