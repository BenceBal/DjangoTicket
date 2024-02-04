# python manage.py test Pages.tests
# or
# python manage.py test Pages

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
        self.customer = ShopCustomer.objects.create(user=self.user, reservations=2,  personalid='12345', firstName='Test', lastName='User', age=25, fanClubMemberid='12345')
        self.match = Match.objects.create(matchName = 'Test Match', eventTime = '2000-01-01', season = 'Test Season')
        self.match_stadium = MatchStadium.objects.create(section='Test Section', capacity=100, matchname=self.match)
        self.ticket = MyTicket.objects.create(matchEvent=self.match_stadium, price=100) 

    def test_add_to_cart(self):
            # Test if tickets can be added to the cart
            self.client.login(username='testuser', password='12345')
            response = self.client.post(reverse('add_to_cart'), {'ticket': [str(self.ticket.Ticketid)]})
            self.assertEqual(response.status_code, 302) 
            self.assertEqual(self.client.session['cart'], [str(self.ticket.Ticketid)])  

    def test_checkout_reserve(self):
        # Test if a ticket can be reserved through checkout
        self.client.login(username='testuser', password='12345')
        session = self.client.session
        session['cart'] = [str(self.ticket.Ticketid)]  # add the ticket to the cart
        session.save()
        response = self.client.post(reverse('checkout'), {'action': 'Reserve', f'ticket_{self.ticket.Ticketid}': str(self.ticket.Ticketid)})
        self.assertEqual(response.status_code, 302)  # 302 because the view redirects after a successful reserve
        self.ticket.refresh_from_db()
        self.assertTrue(self.ticket.reserved)  # check if the ticket is now reserved
        self.assertFalse(self.ticket.bought)  # check if the ticket is not bought
        self.assertEqual(self.ticket.buyer, self.customer)  # check if the ticket's buyer is now the customer
        self.customer.refresh_from_db()
        self.assertGreater(self.customer.reservations, 0)  # check if the customer's reservations have increased by 1
        self.customer.reservations -= 1  # reset the customer's reservations
        session = self.client.session
        self.assertNotIn(str(self.ticket.Ticketid), session['cart'])  # check if the ticket is no longer in the cart

    def test_login_page(self):
        # Test if the login page view returns a 200 status
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)