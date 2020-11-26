from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)

    class Meta:
        model = User
        field = ('username', 'first_name', 'last_name',
                 'email', 'passwprd1', 'password2')
