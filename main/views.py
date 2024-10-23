from django.shortcuts import render
from autentifikasi.models import Profile
from addProduct.models import Food
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
# Create your views here.

@login_required
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
    
    context = {
        'account' : account,
        'foods': sanitized_foods
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
    return HttpResponse(serializers.serialize("xml", data_id), content_type="application/xml")


def show_json_by_id(request, id):
    data_id = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")