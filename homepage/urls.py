from django.urls import path
from homepage.views import show_main, fetch_food

app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),  
    path('fetch-food', fetch_food, name ='fetch_food')
]