from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User 
# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=256,null=True)
    usn = models.CharField(max_length=256,null=True)
    sex = models.CharField(max_length=256,null=True)
    email = models.EmailField(max_length=256,null=True,blank=True)
    branch = models.CharField(max_length=256,null=True,blank=True)
    sem = models.CharField(max_length=256,null=True,blank=True)
    course1 = models.CharField(max_length=256,null=True,blank=True)
    course2 = models.CharField(max_length=256,null=True,blank=True)
    course3 = models.CharField(max_length=256,null=True)
    course4 = models.CharField(max_length=256,null=True)
    course5 = models.CharField(max_length=256,null=True,blank=True)
    course6 = models.CharField(max_length=256,null=True,blank=True)
    course7 = models.CharField(max_length=256,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Personal(models.Model):

    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    avatar = models.CharField(max_length=20,null=True,blank=True,default="dist/img/avatar5.png")
    website = models.CharField(max_length=256,null=True,blank=True)
    github = models.CharField(max_length=256,null=True,blank=True)
    linked = models.CharField(max_length=256,null=True,blank=True)
    bio = models.CharField(max_length=256,null=True,blank=True)

    def __str__(self):
        return self.user.username

