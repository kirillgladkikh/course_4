from django.shortcuts import render

# Create your views here.
# TEST
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет из приложения users!")
