from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Customers.models import ShopCustomer 
from DjangoTicket.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from Ticketshop.models import MyTicket, Match
from django.contrib.auth.decorators import login_required

# Create your views here.


def MainPage(req):
        return render(req, 'MainPage.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            c = ShopCustomer.objects.create(user=user,age=form.cleaned_data["age"],fanClubMemberid=form.cleaned_data["fanclub_id"],personalid=form.cleaned_data["PersonalID"],firstName=form.cleaned_data["username"])

            login(request, user)  # Log in the user after registration
            return redirect(MainPage)  # Redirect to the home page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def mylogout(request):
    logout(request)
    return redirect('main')

# myfunction because namespace collision and non functioning functions
def mylogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def mymain(request):
    return redirect('main')

def myprofile(request):
        return render(request, 'MyProfile.html')

def shop(request):
    tickets = MyTicket.objects.all()
    return render(request, 'Shop.html', {'tickets': tickets})

def cart(request):
    cart = request.session.get('cart', [])
    products = MyTicket.objects.filter(Ticketid__in=cart)
    return render(request, 'cart.html', {'products': products})

@login_required
def order_view(request):
    if request.method == 'POST':
        request.session['cart'] = request.POST
    products = MyTicket.objects.all()
    return render(request, 'order.html', {'products': products})

@login_required    
def add_to_cart(request):
    if request.method == 'POST':
        selected_tickets = request.POST.getlist('ticket')
        cart = request.session.get('cart', [])
        for ticket_id in selected_tickets:
            ticket = MyTicket.objects.get(Ticketid=ticket_id)
            cart.append(str(ticket.Ticketid))
        request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        ticket = get_object_or_404(MyTicket, Ticketid=ticket_id)
        cart = request.session.get('cart', [])
        if str(ticket.Ticketid) in cart:
            cart.remove(str(ticket.Ticketid))
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

@login_required
def checkout(request):
    if request.method == 'POST':
        payment_method = request.POST.get('paymentMethod')

        # Get the age from the user's profile
        age = request.shopcustomer.age

        if age < 18:
            # Apply a 20% discount
            discount = 0.2
        else:
            discount = 0

        # Process the payment...

        return HttpResponse('Payment processed.')
    else:
        return render(request, 'checkout.html')
    
def buy_ticket(request, ticket_id):
    ticket = get_object_or_404(MyTicket, Ticketid=ticket_id)
    # Process the payment...
    ticket.used = True
    ticket.save()
    return render(request, 'confirmation.html', {'ticket': ticket})