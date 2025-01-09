from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('edit-user-info/', views.edit_user_info, name='edit_user_info'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    path('wishlist/add/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]