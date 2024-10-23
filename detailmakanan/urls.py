# detailmakanan/urls.py
from django.urls import path

from review.models import Review
from . import views
from review import views as review_views
from detailmakanan import views

app_name = 'detailmakanan'

urlpatterns = [
    path('review/<uuid:id>/', review_views.food_reviews, name='food_reviews'),  # Use review_views here
    path('<uuid:id>/', views.product_detail, name='product_detail'),
]

