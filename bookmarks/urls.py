from django.urls import path
from .views import add_bookmark,delete_bookmark,bookmark_list,food_list


app_name = 'bookmarks'


urlpatterns = [
    # path('bookmark_list/<uuid:bookmark_id>/', bookmark_list, name='bookmark_list'),
    path('delete_bookmark/<uuid:food_id>/',delete_bookmark, name='delete_bookmark'),
    path('add_bookmark/<uuid:food_id>/', add_bookmark, name='add_bookmark'),
    path('', bookmark_list, name='bookmark_list'),
    path('food-list/', food_list, name='food_list'), 

    
]