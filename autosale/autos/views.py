from django.shortcuts import render
from django.urls import reverse

from .models import Autos

# Create your views here.
def index(request):
    context = {
        "autos": Autos.objects.all()
    }
    return render(request, "autos/index.html", context)