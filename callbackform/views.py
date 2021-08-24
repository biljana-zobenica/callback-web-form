from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_callback_form(request):
    """The home page for callbackform."""
    return render(request, 'callbackform/callbackform.html')

def home(request):
    """The home page for our customers."""
    return render(request, 'main.html')   