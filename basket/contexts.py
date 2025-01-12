from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from bookstore.models import Book


def basket_contents(request):
    """ 
    Context processor to manage basket contents.
    """

    basket_items = []
    total = 0
    book_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity, in basket.items():
        book = get_object_or_404(Book, pk=item_id)
        total += quantity * book.price
        book_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })

    delivery = Decimal(3) if total < 40 else Decimal(0)
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'order_total': total,
        'book_count': book_count,
        'delivery': delivery,
        'free_delivery_threshold': 40,
        'grand_total': grand_total,
        }

    return context
