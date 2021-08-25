from django.forms import ModelForm
from .models import Callback
from django import forms

class CallbackForm(forms.ModelForm):
        name = forms.CharField(max_length= 50, required= True, widget=forms.TextInput(attrs={'class':'form-control'}))
        phone_number = forms.CharField(max_length= 50,required= False, widget=forms.TextInput(attrs={'class':'form-control'}))
        company = forms.CharField(max_length= 70,required= False, widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(max_length= 50, required= True, widget=forms.EmailInput(attrs={'class':'form-control'}))
        subject = forms.CharField(max_length= 200, required= True, widget=forms.TextInput(attrs={'class':'form-control'}))
        problem_description = forms.CharField(max_length= 1000, required= True, widget=forms.TextInput(attrs={'class':'form-control'}))

        class Meta:
            model = Callback
            fields = ('name', 'phone_number', 'company', 'email', 'subject', 'problem_description')
