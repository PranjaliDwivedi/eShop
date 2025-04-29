from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from django.contrib.auth.models import User
from django import forms 

class RegistrationForms(UserCreationForm):
    email = forms.CharField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': "forms-control"}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))