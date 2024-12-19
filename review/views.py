from django.shortcuts import render, get_object_or_404, redirect
from .models import Review 
from main.models import Food
from .forms import ReviewForm
from django.contrib.auth.models import User  # Import user model
from autentifikasi.decorators import role_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Food
from .serializers import ReviewSerializer
from django.http import HttpResponse
from django.core import serializers


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Review, Food
from django.contrib.auth.models import User
import json

@csrf_exempt
def create_review_flutter(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Ambil food berdasarkan ID
            food = Food.objects.get(id=id)

            # Ambil user (gunakan Anonymous jika tidak login)
            if request.user.is_authenticated:
                user = request.user
            else:
                user, _ = User.objects.get_or_create(username='Anonymous', defaults={'password': 'anon'})

            # Buat review baru
            new_review = Review.objects.create(
                food=food,
                user=user,
                rating=data['rating'],
                comment=data['comment']
            )
            new_review.save()

            return JsonResponse({
                "status": "success",
                "message": "Review added successfully!"
            }, status=201)

        except Food.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Food not found."
            }, status=404)
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": f"Error: {str(e)}"
            }, status=400)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=405)



@csrf_exempt
def delete_review_flutter(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            review = Review.objects.get(id=data['id'])
            review.delete()

            return JsonResponse({
                "status": "success",
                "message": "Product deleted successfully!"
            }, status=200)
        except Review.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Product not found."
            }, status=404)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)

@csrf_exempt
def update_review_flutter(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            review = Review.objects.get(id=data['id'])
            review.judul = data['judul']
            review.isi = data['isi']
            review.gambar_url = data.get('gambar_url', None)
            review.save()

            return JsonResponse({
                "status": "success",
                "message": "Product updated successfully!"
            }, status=200)
        except Review.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Product not found."
            }, status=404)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)

def show_review_json(request,id):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# @role_required('buyer')
def food_reviews(request, id):
    food = get_object_or_404(Food, id=id)
    reviews = food.food_reviews.all()  # Fetch all reviews related to this food

    # Calculate average rating
    total_reviews = reviews.count()
    avg_rating = sum(review.rating for review in reviews) / total_reviews if total_reviews > 0 else 0

    if request.method == "POST":
        print(food)
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



def show_json(request, id):
    """
    Function to display JSON data for a specific food item and its reviews.
    """
    try:
        # Fetch the food item by its ID
        food = get_object_or_404(Food, id=id)
        reviews = food.food_reviews.all()  # Fetch related reviews
        
        # Prepare the reviews data
        reviews_data = [
            {
                "user": review.user.username,
                "rating": review.rating,
                "comment": review.comment,
                "date": review.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for review in reviews
        ]
        
        # Calculate average rating
        avg_rating = sum(review.rating for review in reviews) / reviews.count() if reviews else 0

        # Prepare the response
        response_data = {
            "food": {
                "id": str(food.id),
                "name": food.name,
                "price": food.price,
            },
            "reviews": reviews_data,
            "avg_rating": avg_rating,
        }

        # Return the response as JSON
        return JsonResponse(response_data)

    except ObjectDoesNotExist:
        return JsonResponse({"error": "Food not found"}, status=404)