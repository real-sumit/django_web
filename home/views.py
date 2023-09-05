from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Person
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        # else:
        #     return render(request, 'login.html')

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

def contact(request):
    if request.method == "POST":
        # request.POST is a dictionary
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        cnt = Person(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        cnt.save()
        messages.success(request, "The message has been sent!")
    return render(request, "contact.html")

# passing value to the templates 
def test(request):
    context = {
        "variable": "hello! what is your name"
    }
    return render(request, "test.html", context)
    # return HttpResponse("Welcome to our homepage")

# admin 
# pass: admin
