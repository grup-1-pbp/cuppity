from django.shortcuts import render
from main.models import Food
from django.utils.html import strip_tags

def show_main(request):
    foods = Food.objects.all()
    sanitized_foods = []
    for food in foods:
        sanitized_foods.append({
            'name': strip_tags(food.name),
            'id': food.id,
            'restaurant': strip_tags(food.restaurant),
            'price': strip_tags((food.price)), 
            'preference': strip_tags(food.preference),
            'deskripsi': strip_tags(food.deskripsi),
            'image_url': strip_tags(food.image_url) if food.image_url else None
        })
    context = {
        'title': 'Home',  # Page title
        'content': 'Welcome to Mangan Yuk!',  # Welcome message content
        'foods': sanitized_foods,
    }

    return render(request, "main.html", context)
