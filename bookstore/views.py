from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from .models import Book, Review
from .forms import ReviewForm


# Create your views here.


def bookstore(request):
    """
    """

    books = Book.objects.all().order_by('-created_at')
    query = None

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('bookstore:bookstore'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            books = books.filter(queries)

    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': books,
        'search_term': query,
        'page_obj': page_obj,
    }

    return render(request, 'bookstore/bookstore.html', context)




def book_detail(request, book_id):
    """
    """
    
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()
            return redirect('bookstore:book_detail', book_id=book_id)
    
    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }
    
    return render(request, 'bookstore/book_detail.html', context)