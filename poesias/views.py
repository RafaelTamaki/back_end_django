from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse (''' <!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html> ''')

def sobre_view(request):
    return HttpResponse ('somos uma empresa feliz')

def user_view(request, username):
    return HttpResponse (f'nome do usuario: {username}')

