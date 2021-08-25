from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Callback
from .forms import CallbackForm

# Create your views here.

def print_callback_form(request):

    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/confirmation/')

    else:
        form = CallbackForm()
        context = {'form': form}
        return render(request, 'callbackform/callbackform.html', context)


def confirmation(request):
    return render(request, 'confirmation.html')

def home(request):
    return render(request, 'home.html')   
