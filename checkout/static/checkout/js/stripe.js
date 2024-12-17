// Stripe Checkout Integration

// Get Stripe public key and client secret from the template context
const stripePublicKey = document.getElementById("id_stripe_public_key").textContent.trim();
const clientSecret = document.getElementById("id_client_secret").textContent.trim();

// Set up Stripe.js
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const card = elements.create('card');
card.mount('#card-element');

// Display card errors
card.on('change', function (event) {
    const displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Handle form submission
const form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
    event.preventDefault();
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card
        }
    }).then(function (result) {
        if (result.error) {
            document.getElementById('card-errors').textContent = result.error.message;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
