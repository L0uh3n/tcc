from django.forms import ModelForm
from django import forms
from my_app.models import usuario

# Create the form class.
class ClientForm(ModelForm):
    data_nasc = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['nome', 'sobrenome', 'data_nasc', 'usuario', 'senha', 'email', 'num_telefone']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']