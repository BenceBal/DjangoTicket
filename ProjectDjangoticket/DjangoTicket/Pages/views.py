from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.shortcuts import render, redirect
from DjangoTicket.forms import CustomUserCreationForm
from django.contrib.auth import login
from Pages import views
# Create your views here.


def MainPage(req):
        return render(req, 'MainPage.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('')  # Redirect to the home page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})