from django.shortcuts import render
from .models import Cafe

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def write(request):
    return render(request, 'main/write.html')

def cafelist(request):
    cafes = Cafe.objects.all()
    
    context = {
        'cafes': cafes
    }
    return render(request, 'main/cafelist.html', {'cafes': cafes})

def cafedetails(request, pk):
    cafe = Cafe.objects.get(pk=pk)
    
    context = {
        'cafe': cafe,
    }
    
    return render(request, 'main/cafedetails.html', context)