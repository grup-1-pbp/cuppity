
from django.urls import path
from . import views
from addProduct.views import home, add_food, show_xml, show_json, show_xml_by_id, show_json_by_id, edit_food, delete_food

app_name = 'addProduct'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_food/', views.add_food, name='add_food'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:id>/', views.show_xml_by_id, name='show_xml_by_id'),  # Using UUID
    path('json/<uuid:id>/', views.show_json_by_id, name='show_json_by_id'),  # Using UUID
    path('edit-food/<uuid:id>', views.edit_food, name='edit_food'),  # Using UUID
    path('delete-food/<uuid:id>', views.delete_food, name='delete_food'),  # Using UUID
]

