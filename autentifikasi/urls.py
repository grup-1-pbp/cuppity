from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from autentifikasi.views import register, login_user, logout, edit_profile

app_name = 'addProduct'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)