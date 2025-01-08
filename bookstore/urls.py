from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', views.bookstore, name='bookstore'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('add/', views.add_book, name='add_book'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]