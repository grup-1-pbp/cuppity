from django.urls import path
from . import views
# from django.conf import settings
from django.contrib.auth import views as auth_views


app_name = 'autentifikasi'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('home/show_profile', views.show_profile, name="show_profile"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('show_profile', views.show_profile, name="show_profile"),
    path('bookmark/show_profile', views.show_profile, name="show_profile"),
    path('auth/login_app/', views.login_app, name='login_app'),
    path('auth/register_app/', views.register_app, name='register_app'),
    path('auth/user_profile/', views.user_profile, name='user_profile'),

]