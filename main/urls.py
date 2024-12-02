from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:id>/', views.show_xml_by_id, name='show_xml_by_id'),  # Using UUID
    path('json/<uuid:id>/', views.show_json_by_id, name='show_json_by_id'),  # Using UUID
    
    
]