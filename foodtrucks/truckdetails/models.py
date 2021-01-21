from django.db import models

# Create your models here.


class Truck(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    opentime = models.CharField(null=True, blank=True, default='',max_length=500)
    closetime = models.CharField(null=True, blank=True,default='',max_length=500)


