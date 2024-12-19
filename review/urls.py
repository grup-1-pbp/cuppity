from django.urls import path
from review import views

app_name = 'food_reviews'

urlpatterns = [
    path('<uuid:id>/', views.food_reviews, name='food_reviews'),  # Endpoint untuk ulasan makanan
    path('json/<uuid:id>/', views.show_json, name='show_json'),  # Endpoint untuk menampilkan semua JSON tanpa ID
    path('create/<uuid:id>/', views.create_review_flutter, name='create-review'),
    path('review-json/<uuid:id>/',views.show_review_json, name='show-review'),
    path('add-review/<uuid:id>/', views.create_review_flutter, name='create_review_flutter'),
]