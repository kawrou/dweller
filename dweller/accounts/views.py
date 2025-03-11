from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpRequest, HttpResponse

# Create your views here.

def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {"form": form})

def login_view(request: HttpRequest):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('trips')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
