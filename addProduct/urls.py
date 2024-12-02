from django.urls import path
from . import views
from addProduct.views import add_food, edit_food, delete_food, create_product_flutter, update_product_flutter, delete_product_flutter,delete_product_flutter

app_name = 'addProduct'

urlpatterns = [
    
    path('add_food/', views.add_food, name='add_food'),
    path('edit-food/<uuid:id>', views.edit_food, name='edit_food'),  # Using UUID
    path('delete-food/<uuid:id>', views.delete_food, name='delete_food'),  # Using UUID
    path('create-food/', views.create_product_flutter, name='create_product_flutter'),
    path ('update-food/', views.update_product_flutter, name='update_product_flutter'),
    path ('delete-product-flutter/', views.delete_product_flutter, name='delete_product_flutter'),
]
