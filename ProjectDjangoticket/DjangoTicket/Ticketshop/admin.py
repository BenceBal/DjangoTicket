from django.contrib import admin
from .models import MyTicket, SeasonTicket, Match

# Register your models here.

@admin.register(MyTicket)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(SeasonTicket)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Match)
class PersonAdmin(admin.ModelAdmin):
    pass