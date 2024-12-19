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

@login_required
def bookmark_list_flutter(request):
    try:
        profile = request.user.profile
        bookmark, created = Bookmark.objects.get_or_create(profile=profile)
        liked_foods = bookmark.liked_foods.all()

        data = {
            "liked_food": [
                {
                    "id": str(food.id),
                    "name": food.name,
                    "restaurant": food.restaurant,
                    "deskripsi": food.deskripsi,
                    "price": str(food.price),
                    "preference": food.preference,
                    "image_url": food.image_url if food.image_url else "",
                } for food in liked_foods
            ]
        }
        return JsonResponse({
            'status': 'success',
            'data': data
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@csrf_exempt
@login_required
def bookmark_flutter_toggle(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            food_id = data.get('food_id')
            
            if not food_id:
                return JsonResponse({'error': 'Food ID is required'}, status=400)

            profile = request.user.profile
            bookmark, created = Bookmark.objects.get_or_create(profile=profile)

            try:
                food = Food.objects.get(id=food_id)
            except Food.DoesNotExist:
                return JsonResponse({'error': 'Food not found'}, status=404)

            is_bookmarked = bookmark.liked_foods.filter(id=food_id).exists()
            
            if is_bookmarked:
                bookmark.liked_foods.remove(food)
                action = 'removed'
            else:
                bookmark.liked_foods.add(food)
                action = 'added'

            return JsonResponse({
                'status': 'success',
                'message': f'Bookmark {action} successfully',
                'is_bookmarked': not is_bookmarked,
                'food_id': str(food_id)
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


@login_required
def bookmark_list_json(request):
    try:
        profile = request.user.profile
        bookmark, created = Bookmark.objects.get_or_create(profile=profile)
        liked_foods = bookmark.liked_foods.all()

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
            'data': data
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

