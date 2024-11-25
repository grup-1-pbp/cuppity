from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, EditProfileForm
from .models import Profile, User
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from autentifikasi.decorators import role_required
from django.urls import reverse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def register_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password1 = data.get('password1')
            password2 = data.get('password2')
            role = data.get('role', 'buyer')
            budget = data.get('budget', 0)
            profile_image = data.get('profile_image', 'https://tse3.mm.bing.net/th?id=OIP.lLmJV7N4bgAwEBtziWijSQHaJL&pid=Api&P=0&h=180')

            # Check if the passwords match
            if password1 != password2:
                return JsonResponse({
                    "status": False,
                    "message": "Passwords do not match."
                }, status=400)

            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    "status": False,
                    "message": "Username already exists."
                }, status=400)
            print("saaaaaaaa")
            # Create the new user
            user = User.objects.create_user(username=username, password=password1)
            
            # Create the profile
            profile = Profile.objects.create(
                user=user,  # Menggunakan instance User
                role=role,
                profile_image=profile_image,
                budget=budget
            )

            return JsonResponse({
                "username": user.username,
                "status": 'success',
                "message": "User created successfully!"
            }, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({
                "status": False,
                "message": "Invalid JSON format."
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": False,
                "message": f"An error occurred: {str(e)}"
            }, status=500)

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=400)


@csrf_exempt
def login_app(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401) 

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