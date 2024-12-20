from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to update default delivery information.
    """
    class Meta:
        model = UserProfile
        fields = (
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country',
        )
        widgets = {
            'default_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'default_street_address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address 1'}),
            'default_street_address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address 2'}),
            'default_town_or_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Town or City'}),
            'default_county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'County'}),
            'default_postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postcode'}),
            'default_country': forms.Select(attrs={'class': 'form-control'}),
        }
    