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
            return HttpResponseRedirect('/success/')
            #return render(request, 'callbackform/success.html', {})
    else:
        form = CallbackForm()
        context = {'form': form}
        return render(request, 'callbackform/callbackform.html', context)


def print_success(request):
    return render(request, 'callbackform/success.html') 


def home(request):
    return render(request, 'main.html')   
