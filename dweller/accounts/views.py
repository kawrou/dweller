from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import HttpRequest, HttpResponse

# Create your views here.

def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('login')
            return HttpResponse("Signup Page")

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {"form": form})
    #return HttpResponse("Signup Page")
