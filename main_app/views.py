from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import SystemUserForm
from .models import SystemUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    return render(request, template_name='index.html')



def signin_view(request):
    return render(request, template_name='signin.html')




def onbuild_page(request):
    return render(request, template_name='build.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        skill = request.POST.get('skill')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password2 != password:
            messages.warning(request, 'password must match!')
            return redirect('register')

    
        sys_user = SystemUser(
            email=email,
            skill=skill,
            first_name=first_name,
            last_name=last_name,
            
        )

        sys_user.save()
        
        if User:
            new_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            new_user.save()
            
            user = authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return render(request, template_name='signup.html')

















