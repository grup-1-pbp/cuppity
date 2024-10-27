from django.conf import settings
from django.shortcuts import render
from main.models import Food
from django.utils.html import strip_tags
import csv
import os
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

def fetch_food(request):
        with open(os.path.join(settings.BASE_DIR, 'dataset.csv'), newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Food.objects.create(
                    name=row['Produk Makanan'],
                    restaurant=row['Restoran'],
                    deskripsi=row['Lokasi'],
                    price=float(row['Harga']),
                    preference=row['Preferensi'],
                    image_url=row['URL_Gambar']
                )
