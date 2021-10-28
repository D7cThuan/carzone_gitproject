from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,

    }
    return render(request, 'pages/home.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
        }
    return render(request, 'pages/about.html', data)
