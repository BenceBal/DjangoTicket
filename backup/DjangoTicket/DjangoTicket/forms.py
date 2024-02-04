from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Customers.models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    fanclub_id = forms.CharField()
    PersonalID = forms.CharField()
    firstName = forms.CharField(max_length=255)
    lastName = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'password1', 'password2', 'age', 'fanclub_id', 'PersonalID']
