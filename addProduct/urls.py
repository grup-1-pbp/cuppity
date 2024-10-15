from django.urls import path
from . import views

app_name = 'addProduct'  # Namespace for URL resolution

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_food/', views.add_food, name='add_food'),  # Add food page
    path('xml/', views.show_xml, name='show_xml'),  # XML data view
    path('json/', views.show_json, name='show_json'),  # JSON data view
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),  # XML by ID
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),  # JSON by ID
    path('edit_food/<int:id>/', views.edit_food, name='edit_food'),  # Edit food page
]
