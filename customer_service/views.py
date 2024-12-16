from django.contrib import messages
from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.

def customer_service(request):
    """ 
    Handle the customer support form submission.

    """

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been successfully submitted. We will get back to you soon!')
    else:
        form = CustomerForm()

    return render(request, 'customer_service/customer_service.html', {'form': form})
