
const stripePublicKey = document.getElementById("id_stripe_public_key").textContent.trim();
const clientSecret = document.getElementById("id_client_secret").textContent.trim();
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const card = elements.create('card');
const submitButton = document.getElementById("submit-button").textContent.trim();
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
    submitButton.disabled = true;
    const fullName = form.full_name.value.trim();
    const email = form.email.value.trim();

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: fullName,
                email: email,
            },
        }
    }).then(function (result) {
        if (result.error) {
            submitButton.disabled = false;
            document.getElementById('card-errors').textContent = result.error.message;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    }).catch(function (error) {
        // Handle any unexpected errors and re-enable the button
        submitButton.disabled = false;
        console.error("Payment error:", error);
        document.getElementById('card-errors').textContent = "An unexpected error occurred. Please try again.";
    });
});
