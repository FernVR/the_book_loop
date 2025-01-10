from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.

class SellBook(models.Model):
    CONDITION_CHOICES = [
        ('like-new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sell_book_user"
    )
    title = models.CharField(max_length=255)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    country = country = CountryField(blank_label='Country *', null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User Book Sale: ' {self.title} ' from {self.user}"
