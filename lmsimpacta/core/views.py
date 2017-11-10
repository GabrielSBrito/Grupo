from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def matricula(request):
    return render(request,"matricula.html")


