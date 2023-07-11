from django import forms



def validate_of_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('invalid data')

def validate_length(name):
    if len(name)<=5:
        raise forms.ValidationError('invalid length')





class Studentform(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_of_a,validate_length])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[validate_of_a])