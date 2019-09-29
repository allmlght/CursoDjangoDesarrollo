from django import forms

class contacto(forms.Form):
    txtName = forms.CharField(label='txtName', max_length=100)
    txtEmail = forms.CharField(label='txtEmail', max_length=100)
    txtPhone = forms.CharField(label='txtPhone', max_length=100)
    txtSubject = forms.CharField(label='txtSubject', max_length=100)
    txtMsg = forms.CharField(label='txtMsg', max_length=100)