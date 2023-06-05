from django.db import models

# Create your models here.
class Cart(models.Model):
    customerId = models.CharField(max_length=10, default='0')
    totalPrice = models.IntegerField(default=0)

class CartItem(models.Model):
    productId = models.CharField(max_length=10, default='0')
    cartId = models.CharField(max_length=10, default='0')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=100)


