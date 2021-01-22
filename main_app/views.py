from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import SystemUserForm
from .models import SystemUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    return render(request, template_name='index.html')



def signin_view(request):
    return render(request, template_name='signin.html')




def onbuild_page(request):
    return render(request, template_name='build.html')



def register(request):
    print(request.method)
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')
    skill = request.POST.get('skill')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if password2 != password:
        messages.warning(request, 'password must match!')
        return redirect('register')

    else:
        user = SystemUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            skill=skill,
            user=request.user


        )

        user.save()
        user.authenticate()

    return render(request, template_name='signup.html')

















