from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('routes/', views.routes_index, name='routes_index'),
    path('routes/<int:route_id>/', views.routes_detail, name='detail')
]