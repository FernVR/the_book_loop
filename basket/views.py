from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bookstore.models import Book

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """


    return render(request, 'basket/basket.html')


def add_to_basket(request, book_id):
    """
    Add a book to the basket.
    """

    book = get_object_or_404(Book, pk=item_id)
    basket = request.session.get('basket', {})

    if item_id in basket:
        messages.error(request, "This book is already in your basket.")
    else:
        basket[item_id] = 1
        messages.success(request, f'Added "{book.title}" to your basket.')

    request.session['basket'] = basket
    return redirect('book_detail', item_id=item_id)



def remove_from_basket(request, book_id):
    """
    Remove an item from the basket.
    """

    
    


