from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Route
from .forms import SendForm

class RouteCreate(CreateView):
  model = Route
  fields = ['name', 'grade', 'description', 'crag', 'rock_type', 'pitches']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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