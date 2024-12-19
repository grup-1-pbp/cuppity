from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-product/', include('addProduct.urls', namespace='addProduct')),  # Path unik untuk addProduct
    path('review/', include('review.urls', namespace='review')),
    path('', include('addProduct.urls', namespace='addProduct')),  # Namespace sesuai dengan `app_name`
    path('detailmakanan/product-detail/', include('detailMakananfix.urls',namespace='detailMakananfix')), 
    path('', include('autentifikasi.urls',namespace='autentifikasi')),
    path('', include('main.urls',namespace='main')),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('', include('homepage.urls', namespace='homepage')) ,
    path('artikel/', include('artikell.urls', namespace='artikell')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

]
    

    

