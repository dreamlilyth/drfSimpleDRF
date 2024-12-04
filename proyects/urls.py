from django.urls import path
from .api import ProjectViewSet
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.proyecto_list, name='proyecto_list'),
    path('proyectos/new/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/edit/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/delete/', views.proyecto_delete, name='proyecto_delete'),

    path('api/proyectos/', ProjectViewSet.as_view({'get': 'list'}), name='proyecto_api_list'),
    path('api/proyectos/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='proyecto_api_detail'),
]
