from django.shortcuts import render


def frontend(request):
    return render(request, 'frontend.html' )

def index(request):
    return render(request, 'index.html' )

def olma(request):
    return render(request, 'olma.html' )