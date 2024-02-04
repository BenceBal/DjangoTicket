
# python manage.py test Ticketshop.tests

import unittest
from django.test import TestCase
from .services import ProductService
from .models import *

class ProductServiceTest(TestCase):

    def test_instantiation(self):
        # Test if the service can be instantiated
        product_service = ProductService()
        self.assertIsInstance(product_service, ProductService)

    def test_get_all_products(self):
        # Test the get_all_products method
        product_service = ProductService()
        all_products = product_service.get_all_products()
        self.assertIsInstance(all_products, list)

    def test_get_price(self):
        # Test the get_price method
        product_service = ProductService()
        test_product = MyTicket(price=50)  # Create a test product with a known price
        price = product_service.get_price(test_product)
        self.assertEqual(price, 50)

    def setUp(self):
        self.match = Match.objects.create(matchName = 'Test Match', eventTime = '2000-01-01', season = 'Test Season')
        self.match_stadium = MatchStadium.objects.create(section='Test Section', capacity=100, matchname=self.match)
        self.ticket = MyTicket.objects.create(matchEvent=self.match_stadium, price=100)    

    def test_get_by_id_existing(self):
        # Test if a MyTicket instance can be retrieved by its id
        ticket = MyTicket.objects.get(Ticketid=self.ticket.Ticketid)
        self.assertEqual(ticket.Ticketid, self.ticket.Ticketid)
        self.assertEqual(ticket.price, 100)
        self.assertEqual(ticket.matchEvent.matchname.matchName, 'Test Match')
        self.assertEqual(ticket.matchEvent.section, 'Test Section')




