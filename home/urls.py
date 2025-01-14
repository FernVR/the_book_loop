from django.urls import path
from . import views
from .views import robots_txt

urlpatterns = [
    path('', views.home_view, name='home'),
    path("robots.txt", robots_txt),
]