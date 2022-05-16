from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Car
def home(request):
    cars = Car.objects.all()
    return render(request,'home.html',{'cars':cars})

def car_detail(request,id):
    try:
        car=Car.objects.get(id=id)
    except Car.DoesNotExist:
        raise Http404("car not found") 
    return render(request,'car_detail.html',{'car':car})

