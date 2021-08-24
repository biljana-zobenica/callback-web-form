from django.shortcuts import render
from django.http import HttpResponse
from .models import Callback
from .forms import CallbackForm

# Create your views here.

def print_callback_form(request):
    """The home page for callbackform."""
    form = CallbackForm()
    context = {'form': form}
    return render(request, 'callbackform/callbackform.html', context)

def home(request):
    """The home page for our customers."""
    return render(request, 'main.html')   
