from django.shortcuts import render
from autentifikasi.models import Profile
from .models import Food
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
from autentifikasi.models import Profile
import json
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='/homepage')
def home(request):
    if request.user.is_authenticated:
        try:
            account = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            account = None  
    else:
        account = None
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
    account = Profile.objects.get(user=request.user) 
    context = {
        'account' : account,
        'foods': sanitized_foods,
    }
    return render(request, 'home.html', context)

def show_xml(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data_id = Food.objects.filter(pk=id)
    print("web berhasil")
    return HttpResponse(serializers.serialize("xml", data_id), content_type="application/xml")


def show_json_by_id(request, id):
    data_id = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_food = Food.objects.create(
                name=data['name'],
                restaurant=data['restaurant'],
                deskripsi=data['deskripsi'],
                price=price,
                preference=data['preference'],
                image_url=data.get('image_url', None)  # image_url opsional
            )
        new_food.save()

        return JsonResponse({
            "status": "success",
            "message": "Product added successfully!"
        }, status=201)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)

@csrf_exempt
def delete_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        food = Food.objects.get(id=data['id'])
        food.delete()

        return JsonResponse({
            "status": "success",
            "message": "Product deleted successfully!"
        }, status=200)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)
        
@csrf_exempt
def update_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        food = Food.objects.get(id=data['id'])
        food.name = data['name']
        food.restaurant = data['restaurant']
        food.deskripsi = data['deskripsi']
        food.price = data['price']
        food.preference = data['preference']
        food.image_url = data.get('image_url', None)
        food.save()
        
        return JsonResponse({
            "status": "success",
            "message": "Product updated successfully!"
        }, status=200)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)
        
        