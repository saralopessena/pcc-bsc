from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.forms import UserForm, EditUserForm, ProfilePictureForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from .models import ProfilePicture

def list_users(request):
    pass

@login_required(login_url=settings.LOGIN_URL)
def list_users_unique(request):
    user = User.objects.get(id=request.user.id)

    profile_picture = ProfilePicture.objects.get(user=request.user.id)
   
    context = {
        'user': user,
        'profile_picture': profile_picture
    }

    return render(request, 'profile.html', context)

def create_users(request):
    #If que retorna o usuário para a página home caso ele esteja logado
    if request.user.is_authenticated:
        return redirect('/')
    
    profile_picture_form = ProfilePictureForm(request.POST)
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():         
            user = form.save()

            #código pra adicionar a imagem padrão quando o usuário é criado
            picture = profile_picture_form.save(commit=False)
            picture.user = user
            picture.save()

            logout(request)
            return redirect('users:login-users')
        else:
            form = UserForm(request.POST)
            return render(request, 'form_users.html', {'form': form})   
    else:
        form = UserForm()
        return render(request, 'form_users.html', {'form': form})


@login_required(login_url=settings.LOGIN_URL)
def edit_users(request):
    
    user = User.objects.get(id=request.user.id)
    profile_picture = ProfilePicture.objects.get(user=request.user.id)
        

    form = EditUserForm(request.POST or None, instance=user)
    profile_picture_form = ProfilePictureForm(request.POST or None, request.FILES or None, 
                                            instance=profile_picture)

   

    context = {
        'form': form,
        'profile_picture_form': profile_picture_form
    }

    if request.method == 'POST':
        if form.is_valid() and profile_picture_form.is_valid():         
 
            form.save()
            profile_picture_form.save()

            return redirect('users:profile-users')
        else:
            form = UserForm(request.POST)
            return render(request, 'edit_users.html', context)   
    else:
        return render(request, 'edit_users.html', context)

def login_users(request):
    #If que retorna o usuário para a página home caso ele esteja logado
    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            try:
                return redirect(request.POST['next'])
            except MultiValueDictKeyError:
                return redirect('homepage')   
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message
            context = {
                'error': 'Usuário ou senha incorretos'
            }
            return render(request, 'login.html', context)

    else:
        return render(request, 'login.html')

def edit_password(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        
        try:
            user = User.objects.get(username=username)
            if(user.email == email):
                user.set_password(new_password)
                user.save()
                return redirect('users:login-users')
            else:
                context = {
                    'error': 'Credenciais incorretas email'
                }
                return render(request, 'edit_password.html', context) 
        except:
            context = {
                'error': 'Credenciais incorretas'
            }
            return render(request, 'edit_password.html', context)    
    else:
        return render(request,'edit_password.html')

    return render(request,'edit_password.html')

def logout_users(request):
    logout(request)
    return redirect('users:login-users')