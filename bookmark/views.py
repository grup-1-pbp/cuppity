from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
from django.http import JsonResponse
from .models import Bookmark, Food  # Mengimpor model Bookmark dan Food
from autentifikasi.models import Profile  # Mengimpor model Profile
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
def toggle_like(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    profile = request.user.profile  # Assuming Profile is linked to User via OneToOne

    # Get or create the user's bookmark
    bookmark, created = Bookmark.objects.get_or_create(profile=profile)

    if food in bookmark.liked_foods.all():
        bookmark.liked_foods.remove(food)
        liked = False
    else:
        bookmark.liked_foods.add(food)
        liked = True

    return JsonResponse({'liked': liked})

def bookmark_list(request):
    profile = request.user.profile  # Mengambil profil pengguna yang sedang login
    bookmark, created = Bookmark.objects.get_or_create(profile=profile)  # Mengambil atau membuat bookmark
    liked_foods = bookmark.liked_foods.all()  # Mengambil daftar makanan yang disimpan
    return render(request, 'bookmark_list.html', {'liked_foods': liked_foods})