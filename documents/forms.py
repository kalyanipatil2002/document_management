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



class DocumentUploadForm(forms.ModelForm):
    folder_id = forms.ModelChoiceField(
        queryset=Folder.objects.all(),
        label="Select Folder",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Document
        fields = ['title', 'file', 'folder_id']  # Make sure 'folder_id' matches the name used in your template
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']
