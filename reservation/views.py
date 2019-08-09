from django.shortcuts import render
from register.models import Building
from .filters import BuildingFilter

# Create your views here.

def home(request):
    buildings = Building.objects.all()
    filter = BuildingFilter(request.GET, queryset=buildings)
    return render(request, 'home.html', {'buildings' : buildings, 'filter':filter})

def detail(request):
    return render(request, 'detail.html')

def waiting(request):
    return render(request, 'waiting.html')

def base(request):
    return render(request, 'base.html')