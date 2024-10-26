from django.urls import path
from . import views

app_name = 'addProduct'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_food/', views.add_food, name='add_food'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:id>/', views.show_xml_by_id, name='show_xml_by_id'),  # UUID untuk setiap path
    path('json/<uuid:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('edit-food/<uuid:id>/', views.edit_food, name='edit_food'),
    path('delete-food/<uuid:id>/', views.delete_food, name='delete_food'),
]
