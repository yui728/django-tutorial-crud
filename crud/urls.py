from django.urls import path
from . import views

app_name = "crud"
urlpatterns = [
    path('',    views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('edit/<int:editting_id>', views.edit, name='edit'),
]