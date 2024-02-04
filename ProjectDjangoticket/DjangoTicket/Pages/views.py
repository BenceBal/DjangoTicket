from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Customers.models import ShopCustomer 
from DjangoTicket.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from Ticketshop.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q # qomplex queries
from django.contrib import messages
# Create your views here.


def MainPage(request):
    matches = Match.objects.all()  # or any other query to get the matches
    return render(request, 'MainPage.html', {'matches': matches})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            c = ShopCustomer.objects.create(user=user,age=form.cleaned_data["age"],fanClubMemberid=form.cleaned_data["fanclub_id"],personalid=form.cleaned_data["PersonalID"],firstName=form.cleaned_data["firstName"],lastName=form.cleaned_data["lastName"])

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

def shop(request):
    tickets = MyTicket.objects.filter(buyer=None)
    seasontickets = SeasonTicket.objects.filter(buyer=None)
    return render(request, 'Shop.html', {'tickets': tickets, 'seasontickets': seasontickets})

def cart(request):
    cart = request.session.get('cart', [])
    products = MyTicket.objects.filter(Ticketid__in=cart)
    return render(request, 'cart.html', {'products': products})

@login_required
def order_view(request):
    if request.method == 'POST':
        request.session['cart'] = request.POST
    products = MyTicket.objects.all()
    products = SeasonTicket.objects.all()
    return render(request, 'order.html', {'products': products})

@login_required    
def add_to_cart(request):
    if request.method == 'POST':
        selected_tickets = request.POST.getlist('ticket')
        selected_seasontickets = request.POST.getlist('seasonticket')
        cart = request.session.get('cart', [])

        for ticket_id in selected_tickets:
            ticket = MyTicket.objects.get(Ticketid=ticket_id)
            seasonticket = SeasonTicket.objects.all()
            cart.append(str(ticket.Ticketid))
        for seasonticket_id in selected_seasontickets:
            seasonticket = SeasonTicket.objects.get(seasonTicketid=seasonticket_id)
            cart.append(str(seasonticket.seasonTicketid))
        request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        try:
            ticket = get_object_or_404(MyTicket, Ticketid=ticket_id)
        except MyTicket.DoesNotExist:
            # Handle the case where the ticket is not found
            # You can redirect to an error page or display a message
            return HttpResponse("Ticket not found", status=404)

        cart = request.session.get('cart', [])
        if str(ticket.Ticketid) in cart:
            cart.remove(str(ticket.Ticketid))
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')


@login_required
def checkout(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart = request.session.get('cart', [])
        customer = get_object_or_404(ShopCustomer, user=request.user)
        for key in request.POST:
            if key.startswith('ticket_'):
                ticket_id = request.POST[key]
                try:
                    ticket = MyTicket.objects.get(Ticketid=ticket_id)
                except MyTicket.DoesNotExist:
                    ticket = get_object_or_404(SeasonTicket, seasonTicketid=ticket_id)

                if action == 'Buy':
                    ticket.bought = True
                    ticket.reserved = False
                    ticket.buyer = customer            
                elif action == 'Reserve':
                    if customer.reservations >= 5:
                        messages.error(request, 'No more reservations are permitted.')
                        return redirect('cart')
                    ticket.reserved = True
                    ticket.bought = False                
                    ticket.buyer = customer
                    customer.reservations += 1

                ticket.save()
                customer.save()
                if str(ticket.Ticketid) in cart:
                    cart.remove(str(ticket.Ticketid))
        request.session['cart'] = cart
    return redirect('cart')

@login_required
def cancel_reservation(request, ticket_id):
    ticket = get_object_or_404(MyTicket, Ticketid=ticket_id, buyer=request.user.customer.personalid)
    if not ticket.bought:
        ticket.reserved = False
        ticket.buyer = None
        request.user.customer.reservations -= 1
        ticket.save()
        request.user.customer.save()
    return redirect('myprofile')

@login_required
def buy_reservation(request,ticket_id):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        try:
            ticket = MyTicket.objects.get(Ticketid=ticket_id, buyer=request.user.customer.personalid)
        except MyTicket.DoesNotExist:
            ticket = get_object_or_404(SeasonTicket, seasonTicketid=ticket_id, buyer=request.user.customer.personalid)

        # If the ticket is reserved, then it can be bought
        if ticket.reserved:
            ticket.bought = True
            ticket.reserved = False
            ticket.buyer = request.user.customer.personalid
            request.user.customer.reservations -= 1
            ticket.save()
            request.user.customer.save()
            
    return redirect('myprofile')


def myprofile(request):
    if request.user.is_authenticated:
      reserved_tickets = MyTicket.objects.filter(reserved=True, buyer=request.user.customer.personalid)
      bought_tickets = MyTicket.objects.filter(bought=True, buyer=request.user.customer.personalid)
    else:
        bought_tickets = None
        reserved_tickets = None
    return render(request, 'MyProfile.html', {'reserved_tickets': reserved_tickets, 'bought_tickets': bought_tickets})