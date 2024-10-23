from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Review
from .forms import ReviewForm  # You'll create this form next
from django.contrib.auth.decorators import login_required

def food_reviews(request, id):
    food = Food.objects.get(pk=id)
    reviews = food.reviews.all()  # Fetch reviews related to this food item

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.food = food
            review.user = request.user
            review.save()
            return redirect('detailMakananfix:food_reviews', id=food.id)
    else:
        form = ReviewForm()

    # Calculate the average rating (including the initial rating)
    total_reviews = reviews.count()  # Assuming the initial rating is from 100 people
    if total_reviews == 0:
        total_reviews = reviews.count() +1 

    avg_rating = (sum([review.rating for review in reviews]) ) / total_reviews
    

    return render(request, 'reviews.html', {
        'food_id': food.id,
        'reviews': reviews,
        'form': form,
        'avg_rating': avg_rating,
    })
