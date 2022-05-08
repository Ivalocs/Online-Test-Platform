from random import choices
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import register_as

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'username', 'password1', 'password2'
        ]
        labels = {
            'first_name':'Name'
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class RegisterAsForm(forms.ModelForm):
    class Meta:
        model = register_as
        fields = ['who']
        labels = {
            'who' : 'Register As'
        }
    
    def __init__(self, *args, **kwargs):
        super(RegisterAsForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})