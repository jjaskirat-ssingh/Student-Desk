from django import forms
from .models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your search ")