from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Artikel
from .forms import ArtikelForm
from autentifikasi.models import Profile
import json
from django.http import HttpResponse
from django.core import serializers

@csrf_exempt
def create_artikel_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_artikel = Artikel.objects.create(
                judul=data['judul'],
                isi=data['isi'],
                gambar_url=data.get('gambar_url', None)
            )
            new_artikel.save()

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
def delete_artikel_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            artikel = Artikel.objects.get(id=data['id'])
            artikel.delete()

            return JsonResponse({
                "status": "success",
                "message": "Product deleted successfully!"
            }, status=200)
        except Artikel.DoesNotExist:
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
def update_artikel_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            artikel = Artikel.objects.get(id=data['id'])
            artikel.judul = data['judul']
            artikel.isi = data['isi']
            artikel.gambar_url = data.get('gambar_url', None)
            artikel.save()

            return JsonResponse({
                "status": "success",
                "message": "Product updated successfully!"
            }, status=200)
        except Artikel.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Product not found."
            }, status=404)
    else:
        return JsonResponse({
            "status": "failed",
            "message": "Invalid request method."
        }, status=401)

def list_artikel(request):
    artikels = Artikel.objects.all()
    account = Profile.objects.get(user=request.user)
    return render(request, 'artikel.html', {'artikels': artikels, 'account' : account})

def add_artikel(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        gambar_url = request.POST.get('gambar_url')

        if judul and isi and gambar_url:
            Artikel.objects.create(judul=judul, isi=isi, gambar_url=gambar_url)
            return redirect('/artikel')
        else:
            return render(request, 'add_artikel.html', {'error': 'Semua field harus diisi!'})

    return render(request, 'add_artikel.html')

def delete_artikel(request, pk):
    artikel = get_object_or_404(Artikel, pk=pk)  # pk adalah UUID sekarang
    artikel.delete()
    return redirect('/artikel')

@csrf_exempt
def edit_artikel(request, pk):
    artikel = get_object_or_404(Artikel, pk=pk)  # pk adalah UUID sekarang
    if request.method == 'POST':
        form = ArtikelForm(request.POST, instance=artikel)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'invalid_request'})

def show_artikel_json(request):
    data = Artikel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")