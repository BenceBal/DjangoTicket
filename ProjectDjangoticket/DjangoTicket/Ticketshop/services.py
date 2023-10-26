from typing import List
from django.db import models
from Pages.services import IProductService
from .models import MyTicket


# this is the concrete implementation of the IProductService
class ProductService(IProductService):

    def get_all_products(self) -> List[MyTicket]:
        return MyTicket.objects.all()

    def get_price(self, product: MyTicket) -> float:
        # in another product app, the logic for getting the price could be different
        return product.price

    def get_by_id(self, id: str) -> models.QuerySet:
        try:
            return MyTicket.objects.get(id=id)
        except MyTicket.DoesNotExist:
            return None
