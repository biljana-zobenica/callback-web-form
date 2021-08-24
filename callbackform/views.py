from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_callback_form(request):
    """The home page for callbackform."""
    return render(request, 'callbackform/index.html')