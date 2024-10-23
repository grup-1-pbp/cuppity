# detailmakanan/urls.py
from django.urls import path

from review.models import Review
from . import views
from review import views as review_views
from detailMakananfix import views

app_name = 'detailMakananfix'

urlpatterns = [
    path('<uuid:id>/', views.product_detail, name='product_detail'),
]

