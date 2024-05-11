from django import forms 



class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    telefono = forms.CharField(max_length=10, required=True)