
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from Customers.models import *

def hello(req):
    return HttpResponse("HelloWorld")

def registerpage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {}
    return render(request, 'accounts/register.html', context)

def loginpage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
                  
def home(request):

    tickets = ShopCustomer.objects.all()
