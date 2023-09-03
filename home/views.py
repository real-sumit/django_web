from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Person

def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        # request.POST is a dictionary
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        cnt = Person(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        cnt.save()
    return render(request, "contact.html")

# passing value to the templates 
def test(request):
    context = {
        "variable": "hello! what is your name"
    }
    return render(request, "test.html", context)
    # return HttpResponse("Welcome to our homepage")
