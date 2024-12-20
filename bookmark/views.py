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
from autentifikasi.models import User
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

def like_bookmark_flutter(request, id, name):
    food = get_object_or_404(Food, id=id)
    user = User.objects.get(username=name)
    profile = user.profile

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


@login_required
def bookmark_list_json(request, name):
    try:
        # Ambil user berdasarkan username (name)
        user = User.objects.get(username=name)
        
        # Ambil profile berdasarkan user yang ditemukan
        profile = user.profile
        
        # Ambil atau buat Bookmark untuk profile tersebut
        bookmark, created = Bookmark.objects.get_or_create(profile=profile)
        liked_foods = bookmark.liked_foods.all()

        # Siapkan data untuk dikembalikan dalam response JSON
        data = [
            {
                "id": str(food.id),
                "name": food.name,
                "restaurant": food.restaurant,
                "deskripsi": food.deskripsi,
                "price": str(food.price),
                "preference": food.preference,
                "image_url": food.image_url if food.image_url else "",
            }
            for food in liked_foods
        ]

        return JsonResponse({
            'status': 'success',
            'data': data,
        })
    except User.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': f"User with username '{name}' does not exist."
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)