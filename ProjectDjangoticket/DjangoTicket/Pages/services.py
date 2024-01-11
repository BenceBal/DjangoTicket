from django.test import TestCase
from abc import ABC, abstractmethod
from typing import List
from django.db import models
from .models import Ticket

"""
In this code, we are defining the interfaces for the services. 
Interfaces are abstract classes that declare a set of methods that must be implemented 
by any concrete class that implements the interface.
"""


# here we define the interfaces for the services
class IProductService(ABC):
    # Declare abstract methods for ProductService
    @abstractmethod
    def get_all_products(self) -> List[Ticket]:
        pass

    @abstractmethod
    def get_price(self, product: Ticket) -> float:
        pass

    @abstractmethod
    def get_by_Ticketid(self, id: str) -> models.QuerySet:
        pass

class IOrderService(ABC):
    """
    The __init__ method is used in the IOrderService class to initialize an instance of the class.
    It is typically used to set any initial values or attributes that are required by the class.
    In this specific case, it is used to pass an instance of the IProductService class as a parameter
    to the IOrderService constructor.
    This is because the IOrderService class needs to access the get_all_products method of the IProductService class.
    By passing an instance of IProductService to the IOrderService constructor, the IOrderService class can call the
    get_all_products method of the IProductService instance.
    """

    @abstractmethod
    def __init__(self, product_service: IProductService) -> None:
        pass

    @abstractmethod
    def get_all_products(self) -> List[Ticket]:
        pass

    @abstractmethod
    def get_product(self, product_id: int, product_service: IProductService) -> Ticket:
        pass