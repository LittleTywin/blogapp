from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm

from .forms import ProfileUpdateForm,UserRegisterForm, UserUpdateForm
from .models import Profile

def login_view(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING,f'You are already logged in as "{request.user.username}"')
        return redirect(reverse('blog:home'))
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.add_message(request,messages.SUCCESS,f'Welcome back {user.username}.')
                login(request,user)
                return redirect(reverse('blog:home'))
        else:
            form = AuthenticationForm()    

    return render(request, 'users/login.html', {'form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO,f'Logout successful.')
    else:
        messages.add_message(request, messages.INFO,f'You are not logged in.')
    return redirect(reverse('blog:home'))

def register_view(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING,f"You can't register a new user while logged in")
        return redirect(reverse('blog:home'))
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            messages.add_message(request, messages.INFO,f"Welcome {username}! You can now Log In with your new account.")
            return redirect(reverse('users:login'))
        
    else:
        form = UserRegisterForm()
    
    return render(request,'users/register.html',{'form':form})

def profile_view(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO,f'You need to log in to access your profile.')
        return redirect(reverse('users:login'))

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.add_message(request, messages.SUCCESS,f"Profile succesfully updated.")
            return redirect(reverse('users:profile'))

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {'u_form':u_form,'p_form':p_form}


    return render(request,'users/profile.html', context)

