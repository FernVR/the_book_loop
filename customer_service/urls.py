from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_service, name='customer_service'),
]