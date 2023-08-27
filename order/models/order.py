<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

from product.models.product import Product
=======
from django.contrib.auth.models import User
from django.db import models

from product.models import Product

>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a

class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)