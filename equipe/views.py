from django.shortcuts import render

def equipe(request):
    return render(request, 'equipe/equipe.html')