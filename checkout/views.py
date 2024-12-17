from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from bookstore.models import Book
import stripe

# Create your views here.

def checkout(request):
    """
    Render the checkout page and process orders.
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_public_key or not stripe_secret_key:
        messages.error(request, "Stripe payment keys are missing. Please contact support.")
        return redirect(reverse('basket'))

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            # Process basket items and create OrderLineItems
            for item_id, quantity in basket.items():
                book = get_object_or_404(Book, pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    book=book,
                    quantity=quantity,
                    lineitem_total=quantity * book.price
                )

            # Stripe payment processing
            stripe.api_key = stripe_secret_key
            amount = int(order.grand_total * 100)  # Convert to cents
            try:
                stripe.PaymentIntent.create(
                    amount=amount,
                    currency='usd',
                    metadata={'order_id': order.order_number},
                )
            except Exception as e:
                messages.error(request, 'Payment error: ' + str(e))
                return redirect(reverse('checkout'))

            # Clear basket and redirect to success page
            request.session['basket'] = {}
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Please fix the errors in the form.')

    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.info(request, "Your basket is empty.")
            return redirect(reverse('bookstore'))

        # Calculate the order total
        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='usd',
        )

        form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
