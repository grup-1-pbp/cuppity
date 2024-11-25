from django.urls import path
from . import views

app_name = 'artikell'


urlpatterns = [
    path('', views.list_artikel, name='list_artikel'),
    path('add/', views.add_artikel, name='add_artikel'),
    path('delete/<uuid:pk>/', views.delete_artikel, name='delete_artikel'),  # pk adalah UUID
    path('edit/<uuid:pk>/', views.edit_artikel, name='edit_artikel'),  # pk adalah UUID
]
