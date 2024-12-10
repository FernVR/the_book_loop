from django.shortcuts import render

# Create your views here.


def bookstore_home(request):
    return render(request, 'bookstore/bookstore_home.html')