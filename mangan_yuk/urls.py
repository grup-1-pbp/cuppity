from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-product/', include('addProduct.urls', namespace='addProduct')),  # Path unik untuk addProduct
    path('review/', include('review.urls', namespace='review')),
    path('', include('addProduct.urls', namespace='addProduct')),  # Namespace sesuai dengan `app_name`
    path('', include('detailmakanan.urls',namespace='detailmakanan')), 
    path('', include('autentifikasi.urls',namespace='autentifikasi')),
    path('', include('main.urls',namespace='main')),
    path('review/', include('review.urls', namespace='review')),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('', include('homepage.urls', namespace='homepage')) ,
]
    

    

