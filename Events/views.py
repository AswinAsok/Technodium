from django.shortcuts import render
from django.http import HttpResponse

from .models import Event, Registration

# Create your views here.

def home(request):
    Events = Event.objects.all()
    context ={}
    context['Events'] = Events
    return render(request, 'home.html', context)
    #return HttpResponse("This is home page")

def register(request):    
    Registrations = Registration.objects.all()
    context = {}
    context['Registrations'] = Registrations

    total_event = Event.objects.all().count()
    event_names = ()
    for event in range(total_event):
        event_names = event_names + (Event.objects.get(id=event+1).event_name,)
    
    context['Eventnames'] = event_names

    return render(request, 'register.html', context)

