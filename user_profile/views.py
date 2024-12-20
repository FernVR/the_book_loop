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
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your delivery information has been updated.')
        else:
            messages.error(request, 'Update failed. Please check the form for errors.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'user_profile/user_profile.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


def wishlist_view(request):
    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    template = "user_profile/user_profile.html"
    context = {
        "wishlist": wishlist.books.all(),
    }
    return render(request, template, context)


def add_to_wishlist(request):
    if request.method == "POST":
        book = get_object_or_404(Book, id=request.POST.get("book_id"))
        wishlist, _ = WishList.objects.get_or_create(user=request.user)
        wishlist.books.add(book)
    return redirect("wishlist_view")

def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    wishlist = get_object_or_404(WishList, user=request.user)
    wishlist.books.remove(book)
    return redirect("wishlist_view")
