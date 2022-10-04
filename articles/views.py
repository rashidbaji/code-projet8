from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")


def propos(request):
    return render(request, "propos.html")

def connexion (request):
    return render(request, "connexion.html")

def compte (request):
    return render(request, "compte.html")


def contactez (request):
    return render(request, "contactez.html")

def style (request):
    return render(request, "style.css")


 