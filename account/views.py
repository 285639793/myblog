from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm

# Create your views here.

def user_login(request):
    if request.method == "POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse("Welcome You, You have been authenticated successfully")
            else:
                return HttpResponse("Sorry, something must be wrong")
        else:
            return HttpResponse("Invalid Login")
    if request.method == "GET":
        login_form =LoginForm()
        return render(request, "account/login.html", {"form":login_form})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.data['password'])
            new_user.save()
            return HttpResponse("Successfully !")
        else:
            return HttpResponse("You can't register")
    else:
        user_form = RegistrationForm()
        return render(request, "")