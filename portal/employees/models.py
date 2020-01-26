from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pan = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=30)