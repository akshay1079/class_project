from django import forms
from . models import Order

class StudentForm(forms.Form):
    rn = forms.IntegerField()
    name = forms.CharField()
    marks = forms.FloatField()
    city = forms.CharField()
    file = forms.FileField()
class CustomerForm(forms.Form):
    cname = forms.CharField()
    caddr = forms.CharField()
    cemail = forms.EmailField()
    cphone = forms.CharField(max_length=12)
    file = forms.ImageField()

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'          #all fields
       # fields = ('pname','pqty')  #selected fields
    #   exclude = ['pprice']        #exclusion