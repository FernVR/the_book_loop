from django.urls import path
from . import views
from .views import checkout, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('webhook/', webhook, name='webhook'),
]