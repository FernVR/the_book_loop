from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import UserProfile, WishList
from .forms import UserProfileForm
from django.contrib import messages
from bookstore.models import Book

# Create your views here.

@login_required
def user_profile(request):
    """ 
    Returns rendered user profile page

    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishList.objects.filter(user=request.user).first()
    form = UserProfileForm(instance=profile)
    

    template = 'user_profile/user_profile.html'
    context = {
        'profile': profile,
        'wishlist': wishlist.books.all() if wishlist else [],
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_profile(request):
    """
    Allows the user to edit their profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Update failed. Please check the form for errors.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'user_profile/edit_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def wishlist_view(request):
    """ 
    """
    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    template = "user_profile/user_profile.html"
    context = {
        "wishlist": wishlist.books.all(),
    }
    return render(request, template, context)


def add_to_wishlist(request):
    """ 
    """
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        if not book_id:
            messages.error(request, "No book specified.")
            return redirect("wishlist_view")
        try:
            book = get_object_or_404(Book, id=request.POST.get("book_id"))
            wishlist, created = WishList.objects.get_or_create(user=request.user)

            if book in wishlist.books.all():
                messages.warning(request, f"{book.title} is already in your wish-list.")
            else:
                wishlist.books.add(book)
                messages.success(request, f"{book.title} has been added to your wish-list.")
        except Exception as e:
            messages.error(request, "Something went wrong while adding the book to your wish-list.")
            print(f"Error adding to wishlist: {e}")
    else:
        messages.error(request, "Invalid request method.")
    return redirect('bookstore:book_detail', book_id=book_id)


def remove_from_wishlist(request, book_id):
    """
    """
    book = get_object_or_404(Book, id=book_id)
    wishlist = get_object_or_404(WishList, user=request.user)
    wishlist.books.remove(book)
    messages.success(request, f'"{book.title}" has been removed from your wish-list.')
    return redirect("wishlist_view")
