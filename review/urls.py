from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('food/<int:food_id>/', views.review_list, name='review_list'),
    path('food/<int:food_id>/add/', views.add_review, name='add_review'),
    path('food/<int:food_id>/edit/', views.edit_review, name='edit_review'),
    path('food/<int:food_id>/delete/', views.delete_review, name='delete_review'),
    path('food/<int:food_id>/reviews/json/', views.get_reviews_json, name='get_reviews_json'),
]
