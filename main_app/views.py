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





















def send_email(request):
    try:
        email = EmailMessage(
            'Sent from Django App',
            'Testing email sent by maen_techie',
            settings.EMAIL_HOST_USER,
            ['2001stany@gmail.com', 'doccasheby@gmail.com','fredy.masika@gmail.com'],
        )
        email.fail_silently = False
        email.send()
        print('EMAIL GOT SENT')

    except:
        print('NOT SENT')
        return redirect('home')
    
    return render(request, template_name='email.html')