from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Main page view that requires login

def show_main(request):
    context = {
        'title': 'Home',  # Page title
        'content': 'Welcome to Mangan Yuk!',  # Welcome message content
        'user': request.user,  # Passes user data to the template
    }

    return render(request, "main.html", context)

# User logout functionality
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return HttpResponseRedirect(reverse('main:show_main'))

# Optional login view if you want to handle login directly (Django's default login view can also be used)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('main:show_main')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)
