from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'stock') 
    search_fields = ('title',)  
    ordering = ('-created_at',)
    list_editable = ('stock',)

    def save_model(self, request, obj, form, change):
        obj.save()
