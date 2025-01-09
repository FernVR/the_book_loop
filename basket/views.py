from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bookstore.models import Book
from bookstore.views import book_detail
from user_profile.models import WishList

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """


    return render(request, 'basket/basket.html')


def add_to_basket(request, book_id):
    """
    Add a book to the basket.
    """

    book = get_object_or_404(Book, pk=book_id)
    basket = request.session.get('basket', {})

    if book_id in basket:
        messages.error(request, "This book is already in your basket.")
    else:
        basket[book_id] = 1
        messages.success(request, f'Added "{book.title}" to your basket.')

        wishlist = WishList.objects.filter(user=request.user).first()
        if wishlist and book in wishlist.books.all():
            wishlist.books.remove(book)

    request.session['basket'] = basket
    return redirect('view_basket')



def remove_from_basket(request, book_id):
    """
    Remove an item from the basket.
    """

    basket = request.session.get('basket', {})
    
    basket.pop(str(book_id), None)
    request.session['basket'] = basket

    return redirect('view_basket')
    


