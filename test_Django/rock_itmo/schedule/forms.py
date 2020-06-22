from django import forms
from .models import zapis

class zapisForm(forms.ModelForm):

    class Meta:
        model = zapis
        fields = ['name', 'start_time', 'week_day']
 
