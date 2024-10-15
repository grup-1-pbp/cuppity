from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodForm
from .models import Food
from django.http import HttpResponse
from django.core import serializers


def home(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'home.html', context)



def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addProduct:home')  # Use 'app_name:view_name' for namespaced URL resolution
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})


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
    food = get_object_or_404(Food, pk=id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('addProduct:home')  # Use 'app_name:view_name' for namespaced URL resolution
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form})
