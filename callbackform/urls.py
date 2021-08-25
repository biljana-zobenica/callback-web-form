"""Defines URL patterns for callbackforms."""

from django.urls import path
from . import views


urlpatterns = [
    path('confirmation/', views.confirmation),
    path('callbackform/', views.print_callback_form),
    path('', views.home),
]