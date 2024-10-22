from django.urls import path
from . import views
from .views import ReviewList

app_name = 'review'

urlpatterns = [
    path('review/<uuid:food_id>/', views.review_list, name='review_list'),
    path('api/food/<uuid:food_id>/reviews/', ReviewList.as_view(), name='review-list'),
]
