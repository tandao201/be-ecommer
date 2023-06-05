# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# This is our model for user registration.
class product_details(models.Model):
    ### followings are the fields of our table.
    id = models.CharField(max_length=10, primary_key='id')
    product_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.product_category, self.product_name, self.availability, self.price)
