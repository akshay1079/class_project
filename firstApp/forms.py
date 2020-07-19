from django import forms

class StudentForm(forms.Form):
    rn = forms.IntegerField()
    name = forms.CharField()
    marks = forms.FloatField()
    city = forms.CharField()
    email = forms.EmailField()