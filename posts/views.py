from traceback import print_tb
from unicodedata import name
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from posts.forms import PostsForm, CommentsForm
from posts.models import Posts, Comments
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from quiz.models import Quiz
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def detail_posts(request, posts_id):
    post = Posts.objects.get(id=posts_id)
    try:
        quiz = Quiz.objects.get(post=posts_id)
    except Quiz.DoesNotExist:
        quiz = None
    except Exception as err:
        print(err)

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            s_form = form.save(commit=False)
            s_form.post = post
            s_form.user = request.user 
            s_form.save()
            return redirect('posts:detail-posts', posts_id)
        else: 
            return HttpResponse('<h1>Não foi possível criar o comentário</h1>')
    else:   
        form = CommentsForm()
        comments =  Comments.objects.filter(post=posts_id)
        context = {
            'form': form,
            'post': post,
            'quiz': quiz,
            'comments': comments
        }
    return render(request, 'detail_posts.html', context)

@login_required(login_url=settings.LOGIN_URL)
def create_posts(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            s_form = form.save(commit=False)
            s_form.user = request.user
            s_form.save()
            return redirect('/')
        else:
            return HttpResponse('<h1>Não foi possível criar posts</h1>')
    else:   
        form = PostsForm()
        return render(request, 'form_posts.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
def edit_posts(request, posts_id):
    post = Posts.objects.get(id=posts_id)
    form = PostsForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            _history = form.save()
            return redirect(reverse('posts:detail-posts', kwargs={'posts_id': _history.id}))
        else:
            return HttpResponse('<h1>Não foi possível editar posts</h1>')
    else:   
        return render(request, 'form_posts.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
def delete_comments(request, comments_id):
    comments = Comments.objects.get(id=comments_id)
    Comments.objects.get(id=comments_id).delete()
    return redirect('posts:detail-posts', comments.post.id)

@login_required(login_url=settings.LOGIN_URL)
def edit_comments(request, comments_id):
    comments = Comments.objects.get(id=comments_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST or None, instance=comments)
        if form.is_valid():
            form.save()
            return redirect('posts:detail-posts', comments.post.id)
        else:
            return HttpResponse('<h1>Não foi possível editar posts</h1>')
    else:   
        form = CommentsForm(instance=comments)
        return render(request, 'edit_comments.html', {'form': form})
   


"""

0 - lgbt
1 - assedio 
2 - racismo

"""
@login_required(login_url=settings.LOGIN_URL)
def get_page(request, name_page):


    if request.method == "POST":
        message = request.POST['message']
        comments = Comments.objects.create(text=message, user=request.user)
        comments.save()
        return HttpResponseRedirect('#')
    else:
        comments = Comments.objects.all()
        print(comments)
        context = {
            'comments': comments
        }
        return render(request, f'{name_page}.html', context)