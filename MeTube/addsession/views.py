from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def login_view(request):
    #the login view has a list of accounts previously used to log in
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home:home'))
        # Otherwise, return login page again with new context
        else:
            return render(request, "addsession/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "addsession/login.html")

def addsession(request):
    #add a new account to login with
    return render(request, "addsession/addsession.html")

def logout_view(request):
    #logout and return to home
    logout(request)
    return HttpResponseRedirect(reverse('home:home'))