# views.py
from django.shortcuts import render, get_object_or_404
from .models import Food
import review

def product_detail(request, product_id):
    product = get_object_or_404(Food, id=product_id)  # Get the product
    reviews = review.objects.filter(food=product)  # Get reviews related to the product
    return render(request, 'product_detail.html', {'food': product, 'reviews': reviews})
