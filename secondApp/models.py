from django.db import models

# Create your models here.

class college(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

#one to one relations
class College_De(models.Model):
    college = models.OneToOneField(college,on_delete=models.CASCADE)
    rn = models.IntegerField()
    brnch = models.CharField(max_length=30)
    addr = models.CharField(max_length=30)
    yr = models.IntegerField()

    def __str__(self):
        return self.brnch

class Company(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

class Car(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    mname = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.mname


class User(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=30)

    def __str__(self):
        return self.uname
class Community(models.Model):
    user = models.ManyToManyField(User)
    cname = models.CharField(max_length=30)
