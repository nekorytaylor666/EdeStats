from django.db import models


class School(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length = 200)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    ent = models.FloatField(default=0)
# Create your models here.
