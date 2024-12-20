from django.urls import path
from . import views

app_name = 'bookmark'  

urlpatterns = [
    path('like/<uuid:id>/', views.like_bookmark, name='like_bookmark'),
    path('', views.bookmark_list, name='bookmark_list'),
    path('flutter/', views.bookmark_list_flutter, name='bookmark_list_flutter'),
    path('flutter/toggle/', views.bookmark_flutter_toggle, name='bookmark_flutter_toggle'),
    path('json/', views.bookmark_list_json, name='bookmark_list_json'),

]