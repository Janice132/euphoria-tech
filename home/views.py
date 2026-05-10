from django.shortcuts import render

def home(request):
    empresa = "Euphoria Tech"
    return render(request, "home.html", {"empresa": empresa})