from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Artikel
from .forms import ArtikelForm
from autentifikasi.models import Profile

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