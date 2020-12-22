from django.shortcuts import render, redirect
from .models import Route
from .forms import SendForm

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def routes_index(request):
  routes = Route.objects.all()
  return render(request, 'routes/index.html', {'routes': routes})

def routes_detail(request, route_id):
  route = Route.objects.get(id=route_id)
  send_form = SendForm()
  return render(request, 'routes/detail.html', {
    'route': route,
    'send_form': send_form
  })

def add_send(request, route_id):
  form = SendForm(request.POST)
  if form.is_valid():
    new_send = form.save(commit=False)
    new_send.route_id = route_id
    new_send.save()
  return redirect('detail', route_id=route_id)