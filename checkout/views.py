from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from bookstore.models import Book
import stripe
import json
from checkout.webhooks import webhook
from user_profile.models import UserProfile

# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)



def checkout(request):
    """
    Render the checkout page and process orders.
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_public_key or not stripe_secret_key:
        messages.error(request, "Stripe payment keys are missing. Please contact support.")
        return redirect(reverse('view_basket'))

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            # Calculate delivery cost and grand total

            current_basket = basket_contents(request)

            order.order_total = current_basket['total']

            order.delivery_cost = current_basket['delivery']

            order.grand_total = current_basket['grand_total']

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
            amount = int(order.grand_total * 100)
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
            return redirect(reverse('bookstore:bookstore'))
        

        # Retrieve user profile delivery info
        initial_data = {}
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                initial_data = {
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                }
            except UserProfile.DoesNotExist:
                pass

        # Calculate the order total
        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='usd',
        )

        form = OrderForm(initial=initial_data)

    template = 'checkout/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'basket_items': current_basket['basket_items'],
        'order_total': current_basket['total'],
        'delivery_cost': current_basket['delivery'],
        'grand_total': current_basket['grand_total'],
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Renders checkout success page
    Add success message with order number for user.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_success.html', context)

