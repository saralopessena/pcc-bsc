from django.shortcuts import render
from posts.models import Posts

def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts':posts})

def get_page(request, name_page):

    return render(request, f'{name_page}.html')