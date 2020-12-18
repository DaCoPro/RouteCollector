from django.shortcuts import render
from .models import Route

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def routes_index(request):
  routes = Route.objects.all()
  return render(request, 'routes/index.html', {'routes': routes})

