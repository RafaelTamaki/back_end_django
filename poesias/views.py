from django.shortcuts import render
from django.http import HttpResponse
from poesias.utils.factory import fazer_poema

def home_view(request):
    return render(request, 'home.html')

def sobre_view(request):
    return render (request, 'sobre.html')

def contato_view(request):
    return render(request, 'contato.html')

def user_view(request, username):
    return HttpResponse (f'nome do usuario: {username}')

def blog_view(request):
    return render(request, 'blog.html')

def poema_detail(request):
    poetry = fazer_poema()
    return render(request, 'poema_detail.html', {'poetry': poetry})

def poema_list(request):
    poesias = [fazer_poema() for _ in range(5)]
    return render(request, "poema_list.html", {"poesias" : poesias})

def page_extends(request):
    return render(request, 'page_extends.html')