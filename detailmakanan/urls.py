# detailmakanan/urls.py
from django.urls import path

from review.models import Review
from . import views
from review import views as review_views
from detailmakanan import views


app_name = 'detailmakanan'

urlpatterns = [
    path('detailmakanan/product-detail/<uuid:id>/', views.product_detail, name='product_detail'),

    
]
