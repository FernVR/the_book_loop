from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookstore_home, name='bookstore-home'),
]