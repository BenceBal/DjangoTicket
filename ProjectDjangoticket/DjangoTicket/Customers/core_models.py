from django.db import models

# Create your models here.
class Customer(models.Model):
    objects = Core()

    class Meta:
        abstract: True

    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)  
