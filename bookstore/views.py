from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book

# Create your views here.


def bookstore(request):
    """
    """

    books = Book.objects.all().order_by('-created_at')
    paginator = Paginator(books, 12)  # Show 12 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bookstore/bookstore.html', {'page_obj': page_obj})


def book_search(request):
    """
    """
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__icontains=query)  # You can also search by other fields like author
    else:
        books = Book.objects.all()
    
    return render(request, 'bookstore/bookstore.html', {
        'books': books,
        'query': query,
    })


def book_detail(request, id):
    # Retrieve the book by ID or handle a 404 error if not found
    book = get_object_or_404(Book, id=id)
    
    # Pass the book object to the template
    return render(request, 'bookstore/book_detail.html', {'book': book})