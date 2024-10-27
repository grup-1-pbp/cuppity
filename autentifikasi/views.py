from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, EditProfileForm
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
from django.urls import reverse


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:home')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # Hanya POST data, karena tidak ada FILES
        print(request.POST.get('role'))
        if form.is_valid():
            user = form.save()
            print("a")
            print(user)
            profile = Profile.objects.create(
                user=user,
                role=request.POST.get('role'),
                budget=request.POST.get('budget'),
                profile_image=request.POST.get('profile_image')  # Menyimpan URL sebagai teks
                
            )
            profile.save()
   
            messages.success(request, 'Your account has been successfully created!')
            return redirect('autentifikasi:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def edit_profile(request):
    # Ambil instance user dan profile yang sedang login
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None  # Jika profile tidak ditemukan

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user, profile=profile)  # Update user dan profile
        if form.is_valid():
            form.save()

            # Simpan perubahan role, budget, dan URL gambar ke profile
            profile.role = form.cleaned_data.get('role')
            profile.budget = form.cleaned_data.get('budget')
            profile.profile_image = form.cleaned_data.get('profile_image')  # Simpan URL gambar
            profile.save()

            return redirect('main:home')  # Redirect ke halaman home setelah update
    else:
        form = EditProfileForm(instance=user, profile=profile)  # Pre-populate form dengan data user

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'edit_profil.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('autentifikasi:login'))
    response.delete_cookie('last_login')
    return response

def show_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'show_profile.html', {'profile': profile})