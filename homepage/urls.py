from django.urls import path
from homepage.views import show_main, logout_view, login_view  
from django.conf import settings
from django.conf.urls.static import static

app_name = 'homepage'

urlpatterns = [
    path('', show_main, name='show_main'),  
    path('logout/', logout_view, name='logout'),  
    path('login/', login_view, name='login'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
