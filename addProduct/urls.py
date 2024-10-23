from django.urls import path
from . import views
from addProduct.views import home, add_food, show_xml, show_json, show_xml_by_id, show_json_by_id, edit_food, delete_food

app_name = 'addProduct'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_food/', views.add_food, name='add_food'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('edit_food/<int:id>/', views.edit_food, name='edit_food'),
    path('delete_food/<int:id>/', views.delete_food, name='delete_food'),
]
