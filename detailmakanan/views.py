# detailmakanan/views.py
from django.shortcuts import render, get_object_or_404
from main.models import Food
from review.models import Review

def product_detail(request, id):
    food = get_object_or_404(Food, pk=id)  # Fetch the food object using the UUID
    return render(request, 'product_detail.html', {'food': food})

def food_reviews(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    reviews = Review.objects.filter(food=food)

    context = {
        'food': food,
        'reviews': reviews
    }
    
    return render(request, 'food_reviews.html', context)
