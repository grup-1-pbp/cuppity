from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodForm
from .models import Food
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import HttpResponseRedirect

def home(request):
    foods = Food.objects.all()
    sanitized_foods = []
    for food in foods:
        sanitized_foods.append({
            'name': strip_tags(food.name),
            'id': food.id,
            'restaurant': strip_tags(food.restaurant),
            'price': strip_tags((food.price)),  # Convert to string if necessary
            'preference': strip_tags(food.preference),
            'image_url': strip_tags(food.image_url) if food.image_url else None
        })
    
    context = {
        'foods': sanitized_foods
    }
    return render(request, 'home.html', context)

@csrf_exempt
@require_POST
def add_food(request):
    if request.method == "POST":
        name = strip_tags(request.POST.get('name'))
        restaurant = strip_tags(request.POST.get('restaurant'))
        price = strip_tags(request.POST.get('price'))
        preference = strip_tags(request.POST.get('preference'))
        image_url = strip_tags(request.POST.get('image_url')) if request.POST.get('image_url') else None

        # Pastikan price diubah menjadi tipe data Decimal jika di database berupa DecimalField
        food = Food(name=name, restaurant=restaurant, price=price, preference=preference, image_url=image_url)
        food.save()

        return redirect('addProduct:home')  # Redirect ke halaman utama setelah menambahkan produk



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


def edit_food(request, id):
    food = Food.objects.get(pk=id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('addProduct:home')
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form})


def delete_food(request, id):
    food = Food.objects.get(pk=id)
    food.delete()
    return redirect('addProduct:home') 
