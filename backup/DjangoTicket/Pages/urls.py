from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name='main'),  # Main page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('myprofile/', views.myprofile, name='myprofile'),  
    path('ticketshop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
