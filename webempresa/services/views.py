from django.shortcuts import render
from .models import Service
# Create your views here.
def Services(request):
    servicios = Service.objects.all()
    return render(request, "services/services.html", {'servicios':servicios})