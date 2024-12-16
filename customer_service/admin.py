from django.contrib import admin
from .models import CustomerSupport

# Register your models here.

class CustomerSupportAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email')

admin.site.register(CustomerSupport, CustomerSupportAdmin)
