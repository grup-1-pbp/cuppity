
from django.urls import path
from . import views
from addProduct.views import edit_food, delete_food
from main import views as main
app_name = 'addProduct'

urlpatterns = [
    path('', main.home, name='home'),
    path ('add-food/', views.add_food, name='add_food'),
    path('edit-food/<uuid:id>', views.edit_food, name='edit_food'),  # Using UUID
    path('delete-food/<uuid:id>', views.delete_food, name='delete_food'),  # Using UUID
]

