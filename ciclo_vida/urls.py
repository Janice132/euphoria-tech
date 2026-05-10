from django.urls import path
from . import views

urlpatterns = [
    path('', views.ciclo_vida, name='ciclo_vida'),
]