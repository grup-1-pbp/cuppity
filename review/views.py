# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Review
from .forms import ReviewForm
from django.contrib.auth.models import User  # Import user model

def food_reviews(request, id):
    food = get_object_or_404(Food, pk=id)
    reviews = food.food_reviews.all()  # Fetch all reviews related to this food

    # Calculate average rating
    total_reviews = reviews.count()
    avg_rating = sum(review.rating for review in reviews) / total_reviews if total_reviews > 0 else 0

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.food = food

            if request.user.is_authenticated:
                review.user = request.user  # Use logged-in user
            else:
                # Assign 'Anonymous' user if not logged in
                anonymous_user, _ = User.objects.get_or_create(username='Anonymous', defaults={'password': 'anon'})
                review.user = anonymous_user

            review.save()
            return redirect('food_reviews:food_reviews', id=food.id)
    else:
        form = ReviewForm()

    return render(request, 'review_list.html', {
        'food': food,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'form': form,
    })
