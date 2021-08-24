"""Defines URL patterns for callbackforms."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.print_callback_form),
]