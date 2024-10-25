# detailmakanan/views.py
from django.shortcuts import render, get_object_or_404
from addProduct.models import Food

def product_detail(request, id):
    food = get_object_or_404(Food, pk=id)  # Fetch the food object using the UUID
    return render(request, 'product_detail.html', {'food': food})
