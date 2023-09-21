from django.shortcuts import render
from django.http import HttpResponse
from poesias.utils.factory import make_poetry

def home_view(request):
    return render(request, 'home.html')

def sobre_view(request):
    return render (request, 'sobre.html')

def blog_view(request):
    return render(request, 'blog.html')

def poema_detail(request):
    poetry = make_poetry()
    return render(request, 'poema_detail.html', {'poetry': poetry})

def poema_list(request):
    poesias = [make_poetry() for _ in range(5)]
    return render(request, "poema_list.html", {"poesias" : poesias})

def page_extends(request):
    return render(request, 'page_extends.html')