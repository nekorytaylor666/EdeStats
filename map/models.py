from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    ent = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
# Create your models here.
