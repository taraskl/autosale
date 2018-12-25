from django.shortcuts import render
from django.urls import reverse

from .models import Autos

# Create your views here.
def index(request):
    context = {
        "autos": Autos.objects.all(),
    }
    return render(request, "autos/index.html", context)

def mark(request):
    context = {
        "autos": Autos.objects.order_by('mark'),
    }
    return render(request, "autos/index.html", context)    

def model(request):
    context = {
        "autos": Autos.objects.order_by('model'),
    }
    return render(request, "autos/index.html", context)

def price(request):
    context = {
        "autos": Autos.objects.order_by('price'),
    }
    return render(request, "autos/index.html", context)         

def category(request):
    context = {
        "autos": Autos.objects.order_by('category'),
    }
    return render(request, "autos/index.html", context)     

def sort_by_year(request):
    try:
        year_from = int(request.POST["from"])
        year_to = int(request.POST["to"])
        context = {
            "autos": Autos.objects.filter(year__range=(year_from, year_to)),
        }
    except:
        pass
    return render(request, "autos/index.html", context)     
   