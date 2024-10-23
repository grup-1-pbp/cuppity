# detailmakanan/urls.py
from django.urls import path

from review.models import Review
from . import views
from review import views as review_views
from detailmakanan import views

app_name = 'detailmakanan'

urlpatterns = [
<<<<<<< HEAD
    path('review/<uuid:id>/', review_views.food_reviews, name='food_reviews'),  # Use review_views here
    path('<uuid:id>/', views.product_detail, name='product_detail'),
=======
    path('product_detail/<uuid:id>/', views.product_detail, name='product_detail'),
>>>>>>> 9d1706b40df93bd1d77b7661e5e0defaa75a23bf
]

