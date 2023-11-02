from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Customers.models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    fanclub_id = forms.CharField()
    own_id = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'fanclub_id', 'own_id']
