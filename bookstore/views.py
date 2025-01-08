from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from .models import Book, Review
from .forms import ReviewForm, BookForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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
            messages.success(request, "Your review has been submitted.")
            return redirect('bookstore:book_detail', book_id=book_id)
    
    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }
    
    return render(request, 'bookstore/book_detail.html', context)


@login_required
def delete_book(request, book_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Book deleted!')
    return redirect(reverse('bookstore:bookstore'))


@login_required
def edit_book(request, book_id):
    """ Edit a book in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('bookstore:book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to update book. Please ensure the form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.title}')

    template = 'bookstore/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def add_book(request):
    """ Add a book to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('bookstore:book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to add book. Please ensure the form is valid.')
    else:
        form = BookForm()

    template = 'bookstore/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    View to delete a review.
    """
    review = get_object_or_404(Review, pk=review_id)
    
    if review.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")
    
    review.delete()
    messages.success(request, "Your review has been deleted successfully.")
    return redirect('bookstore:book_detail', book_id=review.book.id)
