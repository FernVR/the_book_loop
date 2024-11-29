from django.shortcuts import render
from django.conf import settings
from .models import TestImage

# Create your views here.

def static_test_view(request):
    return render(request, 'testapp/static_test.html')

def media_test_view(request):
    test_image = TestImage.objects.first()  # Get the first uploaded image
    return render(request, 'testapp/media_test.html', {'media_url': test_image.image.url})
