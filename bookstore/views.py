from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

# Create your views here.


def bookstore_home(request):

    books = Book.objects.all().order_by('-created_at')
    paginator = Paginator(books, 12)  # Show 12 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bookstore/bookstore_home.html', {'page_obj': page_obj})