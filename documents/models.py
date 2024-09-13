from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add other fields as needed

    # Specify related_name for the groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Specify a unique related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Specify a unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=255, default='Unnamed Document')
    file = models.FileField(upload_to='files/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
