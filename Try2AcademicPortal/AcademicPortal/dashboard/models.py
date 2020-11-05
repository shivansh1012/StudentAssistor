from django.db import models
from django.utils import timezone
# Create your models here.

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Student(models.Model):
    name = models.CharField(max_length=256,null=True)
    email = models.EmailField(max_length=256,null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class 