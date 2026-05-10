from django.shortcuts import render

def ciclo_vida(request):
    return render(request, 'ciclo_vida/ciclo_vida.html')