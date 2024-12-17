from django.urls import path
from . import views
from .views import checkout

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
]