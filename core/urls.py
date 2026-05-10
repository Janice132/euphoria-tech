from django.contrib import admin
from django.urls import path, include

from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('equipe/', include('equipe.urls')),
    path('processos/', include('processos.urls')),
    path('ciclo-vida/', include('ciclo_vida.urls')),
    path('contato/', include('contato.urls')),

    path('work/', include('portfolio.urls')),  # 👈 adicionado aqui
]