import unittest
from django.test import TestCase
from .services import ProductService
from .models import MyTicket
from Ticketshop import models

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

    def test_get_by_id_existing(self):
        # Test the get_by_id method with an existing ID
        product_service = ProductService()
        test_match = models.Match.objects.create(season='Test Season', matchName='Test Match', capacity=50, capacityFanSector=20)
        # Create a MyTicket object with a valid matchEvent
        test_product = MyTicket.objects.create(price=60, matchEvent=test_match)
        test_product.save()  # Ensure the object is saved
        retrieved_product = product_service.get_by_id(str(test_product.Ticketid))
        self.assertEqual(retrieved_product.price, 60)

    def test_get_by_id_nonexistent(self):
        # Test the get_by_id method with a nonexistent ID
        product_service = ProductService()
        retrieved_product = product_service.get_by_id("nonexistent_id")
        self.assertIsNone(retrieved_product)




