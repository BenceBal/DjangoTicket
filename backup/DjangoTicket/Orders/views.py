from django.shortcuts import render
from Ticketshop.models import MyTicket, SeasonTicket

def order_view(request):
    if request.method == 'POST':
        request.session['cart'] = request.POST
    products = MyTicket.objects.all()
    products.append(SeasonTicket.objects.all())
    return render(request, 'order.html', {'products': products})

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(name__in=cart.keys())
    return render(request, 'cart.html', {'products': products})