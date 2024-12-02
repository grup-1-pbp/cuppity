
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodForm
from main.models import Food
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json



@csrf_exempt
@require_POST
def add_food(request):
    if request.method == "POST":
        # Ambil data dari request POST
        name = strip_tags(request.POST.get('name'))
        restaurant = strip_tags(request.POST.get('restaurant'))
        price = strip_tags(request.POST.get('price'))
        deskripsi = strip_tags(request.POST.get('deskripsi'))
        preference = strip_tags(request.POST.get('preference'))
        image_url = strip_tags(request.POST.get('image_url')) if request.POST.get('image_url') else None

        # Pastikan price diubah menjadi tipe data Decimal jika di database berupa DecimalField
        try:
            food = Food(name=name, restaurant=restaurant, price=price, deskripsi=deskripsi, preference=preference, image_url=image_url)
            food.save()

            # Kembalikan respons JSON jika berhasil
            return JsonResponse({'success': True})
        except Exception as e:
            # Kembalikan respons JSON jika ada error
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    # Kembalikan respons error jika bukan metode POST
    return JsonResponse({'success': False}, status=400)



@role_required('seller')
def edit_food(request, id):
    food = get_object_or_404(Food, pk=id)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Redirect ke halaman home
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form, 'food': food})

@role_required('seller')
def delete_food(request, id):
    food = get_object_or_404(Food,id=id)
    food.delete()
    return redirect('main:home') 


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_food = Food.objects.create(
                name=data['name'],
                restaurant=data['restaurant'],
                deskripsi=data['deskripsi'],
                price=data['price'],
                preference=data['preference'],
                image_url=data.get('image_url', None)  # image_url opsional
            )
            new_food.save()

            return JsonResponse({
                "status": "success",
                "message": "Product added successfully!"
            }, status=201)
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": f"Error: {str(e)}"
            }, status=400)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)

@csrf_exempt
def delete_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            food = Food.objects.get(id=data['id'])
            food.delete()

            return JsonResponse({
                "status": "success",
                "message": "Product deleted successfully!"
            }, status=200)
        except Food.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Product not found."
            }, status=404)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)

@csrf_exempt
def update_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
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
        except Food.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Product not found."
            }, status=404)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)