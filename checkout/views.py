from django.shortcuts import render

# Create your views here.

def checkout(request):
    """
    Render the checkout page.
    """
    return render(request, 'checkout/checkout.html')
