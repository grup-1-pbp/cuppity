from django.urls import path
from . import views
from homepage.views import show_main

app_name = 'homepage'

urlpatterns = [
    path('', views.show_main , name='show_main'),

]
