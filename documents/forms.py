from django import forms
from django.contrib.auth.models import User
from .models import Document, Folder
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Required',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text=None,
    )

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        help_texts = {
            'username': None,
        }



class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']

class FileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file', 'folder']
