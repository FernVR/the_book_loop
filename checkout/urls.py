from django.urls import path
from . import views
from .views import checkout

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('webhook/', views.webhook, name='webhook'),
]