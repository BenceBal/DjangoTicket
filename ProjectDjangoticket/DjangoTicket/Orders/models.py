from django.db import models
from DjangoTicket.settings import PRODUCT_MODEL
from Customers.models import ShopCustomer
from Ticketshop.models import MyTicket, SeasonTicket


class CartSingleTicket(models.Model):
    products = models.ManyToManyField(MyTicket)

class CartSeasonTicket(models.Model):
    products = models.ManyToManyField(MyTicket)

    def __str__(self):
        return "Order id: {self.id}"

class Order(models.Model):
    user = models.OneToOneField(ShopCustomer, on_delete=models.CASCADE, null=True)
    items1 = models.ForeignKey(CartSingleTicket, on_delete=models.CASCADE, blank=True, null=True)
    items2 = models.ForeignKey(CartSeasonTicket, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return " Ordered: {self.user.firstName} {self.user.lastName}"