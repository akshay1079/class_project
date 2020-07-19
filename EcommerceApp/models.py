from django.db import models

# Create your models here.
seller_choices = (
    ('Flipkart','Flipkart'),
    ('Amazon','Amazon'),
    ('Myntra','Myntra'),
    ('Snapdeal','Snapdeal'),
)
class Customer(models.Model):
    cname = models.CharField(max_length=30)
    caddr = models.CharField(max_length=50)
    cemail = models.EmailField()
    cphone = models.CharField(max_length=12)

    def __str__(self):
        return self.cname

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    pname = models.CharField(max_length=30)
    pbatch_no = models.CharField(max_length=30)
    pqty = models.IntegerField()
    pprice = models.FloatField()
    pseller = models.CharField(max_length=30,choices=seller_choices)

    def __str__(self):
        return self.pname
