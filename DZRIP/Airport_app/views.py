from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Flight, Plane


class FlightsView(View):
    def get(self, request):
        flights = Flight.objects.all()
        flight1 = Flight.objects.get(id=1) 
        flight2 = Flight.objects.get(id=2) 
        flight3 = Flight.objects.get(id=3) 
        flight4 = Flight.objects.get(id=4) 
        plane1 = Plane.objects.get(id=1) 
        plane2 = Plane.objects.get(id=2) 
        plane3 = Plane.objects.get(id=3)
        plane4 = Plane.objects.get(id=4)
        return render(request, "flights/master.html", {"master": flights, "flight1": flight1,
        "flight2": flight2,"flight3": flight3,"flight4": flight4,
         "plane1": plane1,"plane2": plane2,"plane3": plane3, "plane4": plane4
        })

class FlightDetailView(View):
    def get(self, request, pk):
        flight = Flight.objects.get(id=pk)
        return render(request, "flights/detail.html", {"flight": flight})