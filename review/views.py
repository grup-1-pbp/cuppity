# reviews/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg
from .models import Review
from .forms import ReviewForm
from addProduct.models import Food
from django.core import serializers

def review_list(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    reviews = food.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    context = {
        'food': food,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1)
    }
    return render(request, 'reviews/review_list.html', context)

@login_required
def add_review(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.food = food
            review.user = request.user
            review.save()
            return redirect('reviews:review_list', food_id=food_id)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'food': food
    }
    return render(request, 'reviews/review_form.html', context)

@login_required
def edit_review(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    review = get_object_or_404(Review, food=food, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:review_list', food_id=food_id)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'food': food,
        'review': review
    }
    return render(request, 'reviews/review_form.html', context)

@login_required
def delete_review(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    review = get_object_or_404(Review, food=food, user=request.user)
    
    if request.method == 'POST':
        review.delete()
    return redirect('reviews:review_list', food_id=food_id)

def get_reviews_json(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    reviews = food.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    reviews_data = serializers.serialize('json', reviews)
    return JsonResponse({
        'reviews': reviews_data,
        'avg_rating': round(avg_rating, 1)
    })