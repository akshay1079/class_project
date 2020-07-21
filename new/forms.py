from django import forms
from django.core import validators

#custom validators..
def marks_validator(m):
    if m%2 != 0:
        raise forms.ValidationError('Marks cant be odd...plz correct it.')

class StudentForm(forms.Form):
    rn = forms.IntegerField(label='Enter your Roll No.',validators=[validators.MinValueValidator(1),
                                        validators.MaxValueValidator(20)],widget=forms.TextInput(attrs={'placeholder':'Enter Roll No.'}))
    name = forms.CharField(label='Enter Name',max_length=30,widget=forms.TextInput(attrs={'placeholder':'FIRST NAME'}))
    marks = forms.FloatField(validators=[marks_validator],label='Enter Marks',widget=forms.TextInput(attrs={'placeholder':'Enter Marks'}))
    pass1 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    pass2 = forms.CharField(label='Enter Password Again',widget=forms.PasswordInput(attrs={'placeholder':'Enter password again'}))
    city = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Enter city..'}))
    about_yourself = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Write here...'}))
'''
    def clean_marks(self):
        entered_marks = self.cleaned_data['marks']
        if entered_marks % 2 != 0:
            raise forms.ValidationError('Marks cant be odd !')
        else:
            return entered_marks

    def clean(self):
        all_data = super().clean()
        p1 = all_data['pass1']
        p2 = all_data['pass2']
        if p1 != p2:
            raise forms.ValidationError('Password didnt matched...')
'''