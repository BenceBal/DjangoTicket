from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

    # Make this class abstract to prevent it from being instantiated directly as it serves as an interface
class Ticket(models.Model):
    class Meta:
        abstract = True

    Ticketid = models.CharField(max_length=10, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.Ticketid:
            self.Ticketid = self.generate_ticketid()
        super(Ticket, self).save(*args, **kwargs)

    def generate_ticketid(self):
        while True:
            id = uuid.uuid4().hex[:10].upper()
            if not self.__class__.objects.filter(Ticketid=id).exists():
                return id

    def __str__(self):
        return self.Ticketid