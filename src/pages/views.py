from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context =  {
        "my_title": "surfingpapi",
        "my_number": 10, 
        "my_list": [8, 23, 24, "Kobe"]
    }
    return render(request, "about.html", my_context)