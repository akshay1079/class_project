from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.FloatField()
    pw = models.CharField(max_length=20)