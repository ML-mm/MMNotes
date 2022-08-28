from django import forms
from .models import Notes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'description', 'author', 'image')


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

