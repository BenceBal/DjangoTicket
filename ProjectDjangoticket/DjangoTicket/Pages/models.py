from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
   
class Ticket(models.Model):

    # Make this class abstract to prevent it from being instantiated directly as it serves as an interface
    class Meta:
        abstract = True

    Ticketid = models.CharField(max_length=10, primary_key=True, default=uuid.uuid4().hex[:10].upper(), editable=False)

    def __str__(self):
        return self.Ticketid