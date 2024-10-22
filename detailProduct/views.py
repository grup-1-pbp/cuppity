from django.shortcuts import render
from .models import Product

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)  # Mengambil detail produk berdasarkan ID
    return render(request, 'product_detail.html', {'product': product})

