const stripePublicKey = document.getElementById("id_stripe_public_key").textContent.trim();
const clientSecret = document.getElementById("id_client_secret").textContent.trim();
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const card = elements.create('card');
const submitButton = document.getElementById("submit-button");

card.mount('#card-element');

// Display card errors
card.on('change', (event) => {
    const displayError = document.getElementById('card-errors');
    displayError.textContent = event.error ? event.error.message : '';
});

// Cache checkout data securely
const cacheCheckoutData = async () => {
    try {
        const response = await fetch('/checkout/cache_checkout_data/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrfToken },
            body: JSON.stringify({
                client_secret: clientSecret,
                save_info: document.getElementById('id-save-info').checked,
            }),
        });
        if (!response.ok) throw new Error('Failed to cache checkout data.');
    } catch (error) {
        console.error('Cache error:', error);
        document.getElementById('card-errors').textContent = 'Error caching checkout data. Please try again.';
    }
};

// Handle form submission
form.addEventListener('submit', async (event) => {
    event.preventDefault();
    submitButton.disabled = true;

    await cacheCheckoutData();

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value.trim(),
                email: form.email.value.trim(),
            },
        },
    }).then((result) => {
        if (result.error) {
            document.getElementById('card-errors').textContent = result.error.message;
            submitButton.disabled = false;
        } else if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }).catch((error) => {
        console.error('Payment error:', error);
        document.getElementById('card-errors').textContent = 'An unexpected error occurred. Please try again.';
        submitButton.disabled = false;
    });
});