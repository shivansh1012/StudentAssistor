# Generated by Django 3.1.2 on 2020-11-05 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20201105_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='branch',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
