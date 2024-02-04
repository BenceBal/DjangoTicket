from django.db import models
from Pages.models import Ticket
from DjangoTicket.settings import PRODUCT_MODEL
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


class BaseTicket(Ticket):
    class Meta:
        swappable = "PRODUCT_MODEL"
        db_table = "products_base"

class Match(models.Model):
    season = models.CharField(max_length=50)
    matchName = models.CharField(max_length=50)  
    eventTime = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField(default=30)
    capacityFanSector = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.matchName}"

class SeasonTicket(models.Model):
    
    seasonTicketid = models.CharField(max_length=10, primary_key=True, default=uuid.uuid4().hex[:10].upper(), editable=False)
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=300)

    def __str__(self):
        return f"{self.seasonTicketid}"   

class MyTicket(BaseTicket):

    class Meta:
        db_table = "pages_ticketbase"

    price = models.IntegerField(default=30)
    used = models.BooleanField(auto_created=True, default=False)
    seasonCard = models.ForeignKey(SeasonTicket, on_delete=models.PROTECT,  null=True, blank=True)
    matchEvent = models.ForeignKey(Match, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Ticketid}"  
 
    @receiver(post_save, sender = Ticket)
    def create_new_ticket(sender, instance, created, **kwargs):
        if created:
            instance.matchEvent.capacity -= 1
            instance.matchEvent.save()
            if instance.matchEvent.capacity > 0:
                MyTicket.objects.create(price=instance.price, seasonCard=instance.seasonCard, matchEvent=instance.matchEvent)

