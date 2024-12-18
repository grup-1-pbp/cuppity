from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
from django.http import JsonResponse
from main.models import Food   
from .models import Bookmark
from autentifikasi.models import Profile  
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from uuid import UUID
import json

@require_POST
@login_required
def like_bookmark(request, id):
    food = get_object_or_404(Food, id=id)
   
    profile = request.user.profile 

    bookmark, created = Bookmark.objects.get_or_create(profile=profile)

    if bookmark.is_food_liked(food):
        bookmark.remove_food(food) 
        liked = False 
    else:
        bookmark.add_food(food)  
        liked = True  


    return JsonResponse({'liked': liked})



def bookmark_list(request):
    profile = request.user.profile
    bookmark, created = Bookmark.objects.get_or_create(profile=profile)
    liked_foods = bookmark.liked_foods.all()
    
    bookmark_name = bookmark.name  
    
    return render(request, 'bookmark_list.html', {
        'liked_foods': liked_foods,
        'bookmark_name': bookmark_name,  
    })

def bookmark_list_flutter(request):
    profile = request.user.profile  # Pastikan user sudah login
    print(profile.name)
    bookmark = Bookmark.objects.get_or_create(profile=profile)  # Pisahkan tuple menjadi dua variabel
    liked_foods = bookmark.liked_foods.all()

    # Buat data yang akan dikirim dalam response
    data = {
        "liked_food": list(liked_foods.values())  # Pastikan mengubah queryset menjadi list agar bisa dikonversi ke JSON
    }
    return JsonResponse({
        'status': 'success',
        'data': data
    })


@csrf_exempt
def bookmark_flutter_toggle(request):
    if request.method == 'POST':
        try:
            # Parse JSON data dari Flutter
            data = json.loads(request.body)
            food_id = data.get('food_id')
            user = request.user

            if not user.is_authenticated:
                return JsonResponse({'error': 'User not authenticated'}, status=401)

            # Ambil atau buat bookmark milik user
            profile = user.profile
            bookmark, created = Bookmark.objects.get_or_create(profile=profile)

            # Ambil objek Food berdasarkan ID
            food = get_object_or_404(Food, id=food_id)

            # Toggle like/unlike
            if food in bookmark.liked_foods.all():
                bookmark.liked_foods.remove(food)
                liked = False
            else:
                bookmark.liked_foods.add(food)
                liked = True

            return JsonResponse({'liked': liked, 'food_id': str(food.id)}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
    
    