from django import forms
from .models import CustomerSupport

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerSupport
        fields = ['full_name', 'email', 'message']