from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    salary = models.IntegerField()


class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    marks = models.FloatField()

    def __str__(self):
        return self.name

class StuD(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    rn = models.IntegerField()
    city = models.CharField(max_length=30)
    yr = models.IntegerField()
