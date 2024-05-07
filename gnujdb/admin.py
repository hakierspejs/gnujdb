from django.contrib import admin
from .models import Gnuj

@admin.register(Gnuj)
class GnujAdmin(admin.ModelAdmin):
    list_display = ('id', 'tytul', 'last_updated')  
    search_fields = ('tytul', 'wartosc', 'wlasnosc', 'miejsce', 'dodatkowe_info')
    list_filter = ('last_updated',)  

