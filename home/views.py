from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contacts(request):
    return render(request, "contacts.html")

# passing value to the templates 
def test(request):
    context = {
        "variable": "hello! what is your name"
    }
    return render(request, "test.html", context)
    # return HttpResponse("Welcome to our homepage")
