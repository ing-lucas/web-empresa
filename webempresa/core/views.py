from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, "core/index.html")

def About(request):
    return render(request, "core/about.html")

def Store(request):
    return render(request, "core/store.html")
