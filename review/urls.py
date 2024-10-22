# reviews/urls.py
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('food/<uuid:food_id>/reviews/', views.review_list, name='review_list'),
    path('food/<uuid:food_id>/add-review/', views.add_review, name='add_review'),
    path('food/<uuid:food_id>/edit-review/', views.edit_review, name='edit_review'),
    path('food/<uuid:food_id>/delete-review/', views.delete_review, name='delete_review'),
    path('api/food/<uuid:food_id>/reviews/', views.get_reviews_json, name='get_reviews_json'),
]