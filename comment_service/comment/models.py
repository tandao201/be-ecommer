from django.db import models

# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=1000, default='')
    productId = models.CharField(max_length=10, default='0')
    createdAt = models.DateTimeField(auto_now_add=True)