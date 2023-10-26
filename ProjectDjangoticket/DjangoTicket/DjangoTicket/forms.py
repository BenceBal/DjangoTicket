from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Customers.models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields: ['First name']