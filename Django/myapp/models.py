from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    icon = models.CharField(max_length=50)
# Create your models here.
