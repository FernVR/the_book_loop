from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', views.bookstore, name='bookstore'),
    path('search/', views.book_search, name='book_search'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]