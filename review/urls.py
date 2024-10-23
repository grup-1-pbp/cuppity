from django.urls import path
from review import views


urlpatterns = [
    path('product_detail/<uuid:id>/', views.product_detail, name='product_detail'),
    path('food_reviews/<uuid:id>/', views.food_reviews, name='food_reviews'),  # Add this line
]
