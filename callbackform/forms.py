from django.forms import ModelForm
from .models import Callback
from django import forms



class CallbackForm(forms.ModelForm):
        required_css_class = 'required'
        name = forms.CharField(max_length= 50, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}))
        phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
        company = forms.CharField(max_length= 70, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(max_length= 50, required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your e-mail address'}))
        subject = forms.CharField(max_length= 200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your subject title'}))
        problem_description = forms.CharField(max_length= 1000, required= True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Describe your issue'}))
        support_date_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])


        class Meta:
            model = Callback
            fields = ('name', 'phone_number', 'company', 'email', 'subject', 'problem_description', 'support_date_time')