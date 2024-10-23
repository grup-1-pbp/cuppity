from django.urls import path
from review import views

app_name = 'review'

urlpatterns = [
    path('<uuid:id>/', views.food_reviews, name='food_reviews'),  # Add this line
]
