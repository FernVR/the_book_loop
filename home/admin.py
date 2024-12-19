from django.contrib import admin
from .models import SellBook

@admin.register(SellBook)
class SellBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'condition', 'price', 'country', 'town_or_city', 'created_on')
    search_fields = ['title', 'user__username']
