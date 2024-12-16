from django.shortcuts import render

# Create your views here.

def home_view(request):
    """
    Renders Home Page. 
    """
    return render(request, 'home/index.html')


def custom_404(request, exception):
    """
    Renders 404 page.
    """
    return render(request, '404.html', status=404)