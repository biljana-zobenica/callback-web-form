from django.forms import ModelForm
from .models import Callback

class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = ('name', 'phone_number', 'company', 'email', 'subject', 
                  'problem_description',)
