
# python manage.py test Customers

from django.test import TestCase
from django.contrib.auth import get_user_model
from Ticketshop.models import ShopCustomer

User = get_user_model()

class ShopCustomerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.shop_customer = ShopCustomer.objects.create(user=self.user, reservations=2,  personalid='12345', firstName='Test', lastName='User', age=25, fanClubMemberid='12345')

    def test_shop_customer_creation(self):
        """Test if a ShopCustomer instance can be created"""
        customer = ShopCustomer.objects.get(user=self.user)
        self.assertEqual(customer.user.username, 'testuser')

    def test_shop_customer_reservations(self):
        """Test if the reservations attribute is correctly updated"""
        customer = ShopCustomer.objects.get(user=self.user)
        customer.reservations += 1
        customer.save()
        self.assertEqual(customer.reservations, 3)