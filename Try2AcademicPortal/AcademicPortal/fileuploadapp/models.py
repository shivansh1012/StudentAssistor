from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class file_upload(models.Model):
	ids=models.AutoField(primary_key=True)
	file_name=models.CharField(max_length=255)
	my_file=models.FileField(upload_to='')

	def ___str__(self):
		return self.file_name

	