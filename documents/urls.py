from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('documents/', views.document_list, name='document_list'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),  
    path('logout/', views.logout_user, name='logout'),
    path('upload/', views.upload_document, name='upload_document'),
    path('create-folder/', views.create_folder, name='create_folder'),
    # path('document_list', views.document_list, name='document_list'),  # '' for default route
    path('<int:pk>/', views.view_document, name='view_document'),
    path('<int:pk>/delete/', views.delete_document, name='delete_document'),
]
