# detailmakanan/urls.py
from django.urls import path
from . import views

app_name = 'detailmakanan'

urlpatterns = [
    path('product-detail/<uuid:id>/', views.product_detail, name='product_detail'),
]
