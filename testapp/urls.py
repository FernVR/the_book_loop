from django.urls import path
from . import views

urlpatterns = [
    path('static-test/', views.static_test_view, name='static-test'),
    path('media-test/', views.media_test_view, name='media-test'),
]
