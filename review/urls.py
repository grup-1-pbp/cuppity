from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('<uuid:food_id>/', views.review_list, name='product_review'),
]
