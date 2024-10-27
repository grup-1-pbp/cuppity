from django.urls import path
from . import views
from addProduct.views import add_food, edit_food, delete_food

app_name = 'addProduct'

urlpatterns = [
    
    path('add_food/', views.add_food, name='add_food'),
    path('edit-food/<uuid:id>', views.edit_food, name='edit_food'),  # Using UUID
    path('delete-food/<uuid:id>', views.delete_food, name='delete_food'),  # Using UUID
]
