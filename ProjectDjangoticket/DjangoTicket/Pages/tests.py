# python manage.py test Pages.tests

from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from Ticketshop.models import *

class HomePageViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_view(self):
        """Test if the home page view returns a 200 status"""
        response = self.client.get('/')  # replace with the actual path to your home view
        self.assertEqual(response.status_code, 200)

User = get_user_model()

class PagesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.match = Match.objects.create(matchName = 'Test Match', eventTime = '2000-01-01', season = 'Test Season')
        self.match_stadium = MatchStadium.objects.create(section='Test Section', capacity=100, matchname=self.match)
        self.ticket = MyTicket.objects.create(matchEvent=self.match_stadium, price=100) 

    def test_add_to_cart(self):
            # Test if tickets can be added to the cart
            self.client.login(username='testuser', password='12345')
            response = self.client.post(reverse('add_to_cart'), {'ticket': [str(self.ticket.Ticketid)]})
            self.assertEqual(response.status_code, 302) 
            self.assertEqual(self.client.session['cart'], [str(self.ticket.Ticketid)])  

    def test_checkout(self):
        # Test if the reservation process works correctly
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/checkout/', {'ticket_id': self.ticket.Ticketid, 'action': "reservation"})  
        self.assertEqual(response.status_code, 200)


    def test_cancel_reservation(self):
        # Test if a reservation can be cancelled
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/cancel_reservation/', {'ticket_id': self.ticket.Ticketid})  # replace with the actual path to your cancel reservation view
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        # Test if the login page view returns a 200 status
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)