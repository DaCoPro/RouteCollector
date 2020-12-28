from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('routes/', views.routes_index, name='routes_index'),
    path('routes/<int:route_id>/', views.routes_detail, name='detail'),
    path('routes/create/', views.RouteCreate.as_view(), name='routes_create'),
    path('routes/<int:pk>/delete/', views.RouteDelete.as_view(), name='routes_delete'),
    path('routes/<int:pk>/update/', views.RouteUpdate.as_view(), name='routes_update'),
    path('routes/<int:route_id>/add_send/', views.add_send, name='add_send')
]