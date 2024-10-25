# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Bookmark
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages


@login_required
def add_bookmark(request, food_id):
    if request.method == 'POST':
        try:
            food = Food.objects.get(id=food_id)
        except Food.DoesNotExist:
            return JsonResponse({'error': 'Food not found'}, status=404)

        # Check if the bookmark already exists
        if Bookmark.objects.filter(food=food, user=request.user).exists():
            return JsonResponse({'status': 'already_exists'}, status=200)
        else:
            Bookmark.objects.create(food=food, user=request.user)
            return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks/bookmark_list.html', {'bookmarks': bookmarks})

@login_required
def delete_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, id=bookmark_id)
    bookmark.delete()
    return redirect('bookmarks:bookmark_list')

def food_list(request):
    foods = Food.objects.all()  # Mengambil semua makanan dari database
    return render(request, 'food_list.html', {'foods': foods})  # Tampilkan template dengan daftar makanan

