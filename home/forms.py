from django import forms
from .models import SellBook

class SellBookForm(forms.ModelForm):
    class Meta:
        model = SellBook
        fields = ['title', 'condition', 'message', 'price', 'country', 'town_or_city' ]