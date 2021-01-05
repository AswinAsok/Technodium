from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


from .models import Event, Registration
from .forms import RegistrationForm

# Create your views here.

def home(request):
    Events = Event.objects.all()
    context ={}
    context['Events'] = Events
    return render(request, 'home.html', context)
    #return HttpResponse("This is home page")

def register(request):    
    context = {}
    Registrations = Registration.objects.all()
    context['Registrations'] = Registrations

    if request.POST:
        form = RegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('register')
            
            
        else:
            form = RegistrationForm()
            context['form'] = form

    else:
        form = RegistrationForm(
            initial={
                'full_name': '',
                'email': '',
                'institute_name': '',
                'github_profile': '',
                'event': ''
            }
        )
        context['form'] = form
    return render(request, 'register.html', context)
    


