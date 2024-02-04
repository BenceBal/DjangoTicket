from django.db import models
from django.contrib.auth.models import  User
import uuid

# python manage.py createsuperuser --username=admin --email=admin@admin.com

class ShopCustomer(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='customer', on_delete=models.CASCADE, null=True)
    personalid = models.CharField(max_length=30, primary_key=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)  
    age = models.IntegerField(null=True, blank=True)
    joined = models.DateField(auto_now_add=True)
    fanClubMemberid = models.CharField(max_length=10, null=True, blank=True)
    reservations = models.IntegerField(default=0)
    seasonticketholder = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

