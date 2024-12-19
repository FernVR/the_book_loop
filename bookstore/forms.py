
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
            'date_published': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
