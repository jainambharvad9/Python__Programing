from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name  = models.CharField(max_length=1000)
    
class Message(models.Model):
    value = models.CharField(max_length=100000)
    data = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=100000)
    room = models.CharField(max_length=100000)