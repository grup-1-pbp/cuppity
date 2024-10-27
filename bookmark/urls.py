from django.urls import path
from . import views

app_name = 'bookmarks'  

urlpatterns = [
    path('like/<uuid:food_id>/', views.toggle_like, name='toggle_like'),
    path('bookmark/', views.bookmark_list, name='bookmark_list'),
]
