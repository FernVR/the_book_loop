from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.contrib import messages

# Create your views here.

@login_required
def user_profile(request):
    """ 
    Returns rendered user profile page

    """
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        messages.success(request, "You don't have a profile")
        return HttpResponseRedirect(reverse('home'))

    template = 'user_profile/user_profile.html'
    context = {
        'profile': profile
    }

    return render(request, template, context)
