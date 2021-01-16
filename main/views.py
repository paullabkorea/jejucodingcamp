from django.shortcuts import render
from .models import Cafe

def index(request):
    context = {
        'locations' : Cafe.locations
    }
    return render(request, 'main/index.html', context)


def cafelist(request):
    selected_locations = request.GET.get('locations')
    
    if selected_locations:
        cafes = Cafe.objects.filter(location__in=selected_locations)
    else:
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