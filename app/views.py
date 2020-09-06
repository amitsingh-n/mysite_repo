from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request, 'display.html', {})

def about (request):
    return render(request, 'about.html', {})

def help (request):
    return render(request, 'help.html', {})
