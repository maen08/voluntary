from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings


def home_view(request):
    return render(request, template_name='index.html')



def signin_view(request):
    return render(request, template_name='signin.html')



def signup_view(request):
    return render(request, template_name='signup.html')


def onbuild_page(request):
    return render(request, template_name='build.html')





















