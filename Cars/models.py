from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length = 30, primary_key = True)
    brand_descr = models.TextField(null=True, blank=True)
    brand_rating = models.FloatField(null=True, blank=True)

class Car(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    top_speed = models.IntegerField()
    mileage = models.FloatField()
    cost = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = 'Cars', null = True)
    description = models.TextField()
    quantity = models.IntegerField()
