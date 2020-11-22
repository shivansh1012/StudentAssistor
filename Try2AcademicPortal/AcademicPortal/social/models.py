from django.db import models

# Create your models here.
class document_upload(models.Model):
    BRANCH = [
        ('CST','CST'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('BCA','BCA'),
        ('Aerospace','Aerospace'),
        ('Mechanical','Mechanical')
    ]

    SEMESTER=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    ]

    branch = models.CharField(max_length=255,null=True,choices=BRANCH)
    semester = models.CharField(max_length=255,null=True,choices=SEMESTER)
    course = models.CharField(max_length=255,null=True)
    file_name = models.CharField(max_length=255,null=True)
    my_file = models.FileField(upload_to='')

    def __str__(self):
        return self.file_name

	