from django.db import models

# Create your models here.
class Profile(models.Model):
    name     = models.CharField(max_length=100,blank=False)
    email    = models.EmailField(blank=False)
    username = models.CharField(max_length=100,blank=False)
    password = models.CharField(max_length=100,blank=False,default=1234)