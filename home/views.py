from django.shortcuts import render
from django.contrib import messages
from .forms import SellBookForm
from bookstore.models import Book
import random

# Create your views here.

def home_view(request):
    """
    Renders Home Page. 
    Handles Sell book form
    Handles best seller section
    """

    form = SellBookForm()
    if request.method == 'POST':
        form = SellBookForm(request.POST)
        if form.is_valid():
            sell_book = form.save(commit=False)
            sell_book.user = request.user
            sell_book.save()
            messages.success(request, 'Your book has been successfully submitted!')
            form = SellBookForm()
    
    all_books = list(Book.objects.all())
    best_seller_books = random.sample(all_books, min(3, len(all_books)))

    context = {
        'form': form,
        'best_seller_books': best_seller_books,
    }

    return render(request, 'home/index.html', context)


def custom_404(request, exception):
    """
    Renders 404 page.
    """
    return render(request, '404.html', status=404)