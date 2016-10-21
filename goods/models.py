from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producer(models.Model):
    COUNTY = (
        ('AUS', 'Austrilia'),
        ('NZ', 'New Zealand'),
    )
    producer_name = models.CharField(max_length=100,unique=True)
    produced_country = models.CharField(max_length=3, choices=COUNTY)
    def __unicode__(self):
       return self.producer_name

class Brand(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100,unique=True)
    def __unicode__(self):
       return self.producer.producer_name + ":" + self.brand_name

class Product(models.Model):    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __unicode__(self):
       return self.brand.producer.producer_name + ":" + self.brand.brand_name + self.product_name
    
