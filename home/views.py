from django.shortcuts import render
from .forms import SellBookForm

# Create your views here.

def home_view(request):
    """
    Renders Home Page. 
    """

    form = SellBookForm()
    if request.method == 'POST':
        form = SellBookForm(request.POST)
        if form.is_valid():
            sell_book = form.save(commit=False)
            sell_book.user = request.user
            sell_book.save()


    return render(request, 'home/index.html', {'form': form})


def custom_404(request, exception):
    """
    Renders 404 page.
    """
    return render(request, '404.html', status=404)