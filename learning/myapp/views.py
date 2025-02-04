from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm, SignupForm

# Home page view (index page)
def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'index.html')

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        print("testing")
        if login_form.is_valid():
            print("valid")
            print(login_form.cleaned_data.get("username"))
            print(login_form.cleaned_data.get("password"))
            authenticated_user = authenticate(request, username=login_form.cleaned_data.get("username"), password=login_form.cleaned_data.get("password"))
            print(authenticated_user)
            if authenticated_user is not None:
                login(request=request, user=authenticated_user)
                print("logged in")
            return HttpResponseRedirect("/")


    return render(request, 'login.html')


def signout_view(request):
    logout(request)
    return HttpResponseRedirect("/") 


def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            if User.objects.filter(username = signup_form.cleaned_data.get("username")).first():
                return render(request, 'signup.html')
            

            user = User.objects.create_user(signup_form.cleaned_data.get("username"), password=signup_form.cleaned_data.get("password"))

            authenticated_user = authenticate(request, username=signup_form.cleaned_data.get("username"), password=signup_form.cleaned_data.get("password"))
            if authenticated_user is not None:
                login(request=request, user=authenticated_user)
            return HttpResponseRedirect("/")

    return render(request, 'signup.html')


