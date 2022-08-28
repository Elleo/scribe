from dal import autocomplete
from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['name', 'image', 'language', 'script', 'prioritise_accuracy']
