from django.contrib import admin

# Register your models here.
from . models import * 
admin.site.register(Document)
admin.site.register(Folder)
admin.site.register(CustomUser)