from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Review
from .forms import ReviewForm  # Make sure this form exists and works
from django.contrib.auth.decorators import login_required

@login_required
def food_reviews(request, id):
    food = get_object_or_404(Food, pk=id)  # Safely fetch the food object or return 404
    reviews = food.review_set.all()  # Access related reviews using the default reverse relation

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.food = food
            review.user = request.user  # Ensure the user is logged in (handled by login_required)
            review.save()
            return redirect('detailMakananfix:food_reviews', id=food.id)  # Make sure this URL is correctly configured
    else:
        form = ReviewForm()

    # Calculate the average rating, including the initial rating from 100 people
    total_reviews = reviews.count()
    initial_ratings = 100  # Initial ratings from 100 people

    if total_reviews > 0:
        avg_rating = (sum([review.rating for review in reviews]) + initial_ratings) / (total_reviews + 1)
    else:
        avg_rating = initial_ratings  # Default average when there are no reviews yet

    return render(request, 'reviews/review_form.html', {
        'food_id': food.id,
        'reviews': reviews,
        'form': form,
        'avg_rating': avg_rating,
    })
