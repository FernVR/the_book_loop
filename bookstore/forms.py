
from django import forms
from .models import Review, Book

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_published', 'description', 'condition', 'rating', 'price', 'cover_image', 'stock']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'date_published': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
