from django.db import models
from Pages.models import Ticket
from DjangoTicket.settings import PRODUCT_MODEL
from Customers.models import ShopCustomer
import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta

class BaseTicket(Ticket):
    class Meta:
        swappable = "PRODUCT_MODEL"
        db_table = "products_base"

class Match(models.Model):
    season = models.CharField(max_length=50)
    matchName = models.CharField(max_length=50)  
    eventTime = models.DateField(default=(datetime.now() + relativedelta(months=1)).date())

    def __str__(self):
        return f"{self.matchName} // {self.eventTime}"
    
    def save(self, *args, **kwargs):
        is_new = not self.pk  # Check if it's a new instance
        super().save(*args, **kwargs)  # Call the "real" save() method.

        if is_new:
            # If it's a new instance, create the MatchStadium instances
            MatchStadium.objects.create(matchname=self, capacity=50, section='A')
            MatchStadium.objects.create(matchname=self, capacity=50, section='B')
            MatchStadium.objects.create(matchname=self, capacity=50, section='C')
            MatchStadium.objects.create(matchname=self, capacity=10, section='F')

class MatchStadium(models.Model):
    capacity = models.IntegerField(default=30)
    section = models.CharField(max_length=2, default="A")
    matchname = models.ForeignKey(Match, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.matchname} // {self.section}"

class SeasonTicket(models.Model):
    
    seasonTicketid = models.CharField(max_length=10, primary_key=True, default=uuid.uuid4().hex[:10].upper(), editable=False)
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=300)
    bought = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)
    buyer = models.ForeignKey(ShopCustomer, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.seasonTicketid}"   

class MyTicket(BaseTicket):

    class Meta:
        db_table = "pages_ticketbase"

    price = models.IntegerField(default=30)
    used = models.BooleanField(auto_created=True, default=False)
    seasonCard = models.ForeignKey(SeasonTicket, on_delete=models.PROTECT,  null=True, blank=True)
    matchEvent = models.ForeignKey(MatchStadium, on_delete=models.PROTECT)
    bought = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)
    buyer = models.ForeignKey(ShopCustomer, on_delete=models.PROTECT, null=True, blank=True)
    
        
    def __str__(self):
        return f"{self.Ticketid} // {self.matchEvent.matchname} // {self.buyer}"  

    def save(self, *args, **kwargs):
        if self.pk is not None:  # Check if it's an existing instance
            orig = MyTicket.objects.get(pk=self.pk)
            if orig.bought == False and self.bought == True:  # Check if the ticket was just bought
                # Decrease the capacity of the MatchStadium
                self.matchEvent.capacity -= 1
                self.matchEvent.save()

                # Create a new ticket with a new ID
                new_ticket = MyTicket.objects.create(
                    price=self.price,
                    used=False,
                    seasonCard=None,
                    matchEvent=self.matchEvent,
                    bought=False,
                    reserved=False,
                    buyer=None,
                )

        super().save(*args, **kwargs)  # Call the "real" save() method.

