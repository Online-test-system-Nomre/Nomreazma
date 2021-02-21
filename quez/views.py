from django.shortcuts import render

# Create your views here.
#inputT


def index(request):
    context = {}
    return render(request, 'index.html', context)

def error404(request): # new, for 404 error
    context = {}
    return render(request, '404.html', context)