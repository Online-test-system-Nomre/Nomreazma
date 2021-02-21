from django.shortcuts import render

# Create your views here.
#inputT


def index(request):
    context = {}
    return render(request, 'index.html', context)
