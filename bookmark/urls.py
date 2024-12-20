from django.urls import path
from . import views

app_name = 'bookmark'  

urlpatterns = [
    path('like/<uuid:id>/', views.like_bookmark, name='like_bookmark'),
    path('', views.bookmark_list, name='bookmark_list'),
    path('json/<str:name>/', views.bookmark_list_json, name='bookmark_list_json'),
    path('json/<str:name>/<uuid:id>/', views.like_bookmark_flutter, name='bookmark_toggle_json'),
]