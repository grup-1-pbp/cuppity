from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-product/', include('addProduct.urls', namespace='addProduct')),  # Path unik untuk addProduct
    path('review/', include('review.urls', namespace='review')),
    path('', include('addProduct.urls', namespace='addProduct')),  # Namespace sesuai dengan `app_name`
    path('product-detail/', include('detailMakananfix.urls')),
    path('review/', include('review.urls', namespace='review')),
]
