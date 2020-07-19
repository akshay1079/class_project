from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=30)
    mark = models.FloatField()

    def __str__(self):
        return self.name
        #return f'Rn={self.rn},name={self.name},mark={self.mark}'

#relation one to one...
class Student_Details(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    salary = models.IntegerField()

# relation one to many...
class Company(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

class Cars(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    mname = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.mname


#relation many to  many...
class User(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=30)

    def __str__(self):
        return self.uname

class Community(models.Model):
    user = models.ManyToManyField(User)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname