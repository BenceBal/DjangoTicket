from typing import List
from Pages.services import IProductService
from .models import MyTicket

class ProductService(IProductService):

    def get_all_products(self) -> List[MyTicket]:
        return list(MyTicket.objects.all())

    def get_price(self, product: MyTicket) -> float:
        return product.price

    def get_by_id(self, id: str) -> MyTicket:
        queryset = MyTicket.objects.filter(Ticketid=id)
        if queryset.exists():
            return queryset.first()
        else:
            return None

    def get_by_Ticketid(self, Ticketid: str) -> MyTicket:
        try:
            return MyTicket.objects.get(Ticketid=Ticketid)
        except MyTicket.DoesNotExist:
            return None
