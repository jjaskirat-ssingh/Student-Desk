from django import forms
# from .forms import ModelFormWithFileField
from .models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'file']
# class NotesForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     description = forms.CharField(max_length=200)
#     file = forms.FileField()

class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        fields = ['title', 'description', 'subject', 'file']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your search ")

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        