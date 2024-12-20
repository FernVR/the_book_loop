from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

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
