from django.urls import path
from review import views

app_name = 'food_reviews'

urlpatterns = [
    path('<uuid:id>/', views.food_reviews, name='food_reviews'),  # Add this line
]
