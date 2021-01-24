from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .models import SystemUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from .models import SystemActivitie, SystemUser


def home_view(request):
    return render(request, template_name='index.html')


# def signin_view(request):
#     return render(request, template_name='signin.html')


def onbuild_page(request):
    return render(request, template_name='build.html')


def apply_activity(request):  # will be triggered by the apply

    # clicked button by applicant

    queryset = SystemActivitie.objects.all()

    # check the number of existing/successful applicants
    # compare to the remaining chance, if true apply if not reject

    return redirect('#')  # redirect to his profile


# def applied_activity(request):
#     activities = SystemActivitie.objects.all()
#     users = SystemUser.objects.all()

#     args = {
#         'activities': activities,
#         'users':users
#     }
#     return render(request, template_name='applied-activity.html', context=args)


def applied_activity(request):
    return render(request, template_name='done.html')






def display_activity(request):

    activities = SystemActivitie.objects.all()

    args = {
        'activities': activities
    }

    return render(request, template_name='activity.html', context=args)


def create_activity(request):
    if request.method == 'POST':
        title = request.POST.get('title')   # display time added
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        place = request.POST.get('place')
        requirement = request.POST.get('requirement')
        no_people = request.POST.get('no_people')
        organization = request.POST.get('organization')

        activity = SystemActivitie(
            activity_name=title,
            description=description,
            requirement=requirement,
            place=place,
            duration=duration,
            people_required=no_people,
            organization=organization,

            # time=str(datetime.now)     # double check the field


        )
        
        activity.save()
        # try:
        # activity.save()
        messages.success(request, 'New jobs created !')

        # except:
        # messages.warning(request, 'New jobs not created')

        # create this page
    return render(request, template_name='create_activity.html')


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
            messages.warning(request, 'Passwords must match!')
            return redirect('register')

        if not '@' and '.' in email:
            messages.warning(request, 'Invalid email!')
            return redirect('register')

        filter_username = User.objects.filter(username=username)
        if filter_username:
            messages.warning(request, 'This username has already taken!')
            return redirect('register')

        sys_user = SystemUser(
            email=email,
            skill=skill,
            first_name=first_name,
            last_name=last_name
            # user=request.user

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
            return redirect('new_activity')


    return render(request, template_name='signup.html')


def login_view(request):    #not real authenticate the password
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        filter_username = User.objects.filter(username=username)
        if not filter_username:
            messages.warning(request, 'You dont have an account, please register!')
            return redirect('register')

        user = authenticate(
            request,
            username=username,password=password
        )
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('new_activity')


    return render(request, template_name='login.html')
