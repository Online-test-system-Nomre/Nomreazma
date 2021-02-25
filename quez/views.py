from django.shortcuts import render
from requests import get

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)
