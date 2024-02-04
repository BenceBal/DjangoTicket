from django.contrib import admin
from .models import ShopCustomer

# Register your models here.

admin.site.register(ShopCustomer)
class SeasonTicketAdmin(admin.ModelAdmin):
    save_as = True  
