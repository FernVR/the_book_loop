from django.shortcuts import render, redirect, get_object_or_404
from bookstore.models import Book

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """

    basket = request.session.get('basket', {})
    basket_items = []

    for book_id, quantity in basket.items():
        book = get_object_or_404(Book, id=book_id)
        basket_items.append({
            'book': book,
            'quantity': quantity,
        })

    return render(request, 'basket/basket.html', {'basket_items': basket_items})


def add_to_basket(request, book_id):
    """
    """

    book = get_object_or_404(Book, id=book_id)
    if 'basket' not in request.session:
        request.session['basket'] = {}
    basket = request.session.get('basket', {})
    basket[str(book.id)] = basket.get(str(book.id), 0) + 1
    request.session['basket'] = basket
    return redirect('view_basket')

def remove_from_basket(request, book_id):
    """
    """

    basket = request.session.get('basket', {})
    if str(book_id) in basket:
        del basket[str(book_id)]
    request.session['basket'] = basket
    return redirect('view_basket')
