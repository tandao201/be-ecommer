from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    book_name = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    publishAt = models.CharField(max_length=45)
    price = models.IntegerField()
    quantity = models.IntegerField()
