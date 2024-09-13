from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import  FolderForm,FileForm
from .models import Document, Folder
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth.decorators import login_required
from .models import Document, Folder
from django.db import IntegrityError

def dashboard(request):
    return render(request, 'dashboard.html')

def document_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated
    
    # Assuming you have logic to display the document list
    return render(request, 'document_list.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in immediately after registration
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('document_list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})
def logout_user(request):
    logout(request)
    return redirect('login') 

# @login_required
# def upload_document(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = form.save(commit=False)
#             file.owner = request.user
#             file.save()
#             return redirect('file_list')
#     else:
#         form = FileForm()
#     return render(request, 'upload.html', {'form': form})
@login_required
def upload_document(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user  # Set the user
            document.save()
            return redirect('document_list')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})



@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'document_list.html', {'documents': documents})
@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('document_list')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

# @login_required
# def document_list(request):
#     documents = Document.objects.filter(user=request.user)
#     folders = Folder.objects.filter(user=request.user)
#     return render(request, 'document_list.html', {'documents': documents, 'folders': folders})

@login_required
def view_document(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    return render(request, 'view_document.html', {'document': document})

@login_required
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    document.delete()
    return redirect('document_list')
