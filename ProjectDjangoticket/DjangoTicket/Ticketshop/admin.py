from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(MyTicket)
class MyTicketAdmin(admin.ModelAdmin):
    save_as = True  # Enable 'Save as new' button

@admin.register(SeasonTicket)
class SeasonTicketAdmin(admin.ModelAdmin):
    save_as = True  

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    save_as = True  

# For Use Case 2,  was save_as added

@admin.register(MatchStadium)
class MatchAdmin(admin.ModelAdmin):
    save_as = True  