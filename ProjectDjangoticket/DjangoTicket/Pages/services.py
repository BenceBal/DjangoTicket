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