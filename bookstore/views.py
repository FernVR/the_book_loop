from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Book, Review
from .forms import ReviewForm

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
            return redirect('bookstore/book_detail', id=id)
    
    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }
    
    return render(request, 'bookstore/book_detail.html', context)