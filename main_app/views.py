from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from .models import SystemUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from .models import SystemActivitie, SystemUser
from django.views.generic.base import RedirectView
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
import json





def cancel_view(request, item_id):
    cancel = SystemActivitie.objects.filter(pk=item_id)

    # cancel.delete()
    # print(cancel.delete())

    messages.success(request, 'Activity cancelled!')
    return render(request, template_name='applied-activity.html', context=args)




def apply_view(request, activity_id):
    get_activity = get_object_or_404(SystemActivitie, pk=activity_id)
    applied_people = get_activity.apply_number.add(
        request.user)                    # just save in DB the user who applied

    print(get_activity)
    request.session['name']=str(get_activity)

    messages.success(request, 'Success, Activity added!')
    titles=SystemActivitie.objects.filter(
        apply_number=request.user)

    request.session['title']=str(titles)

    return redirect('new_activity')




def applied_activity(request):
    activities=SystemActivitie.objects.all()
    users=SystemUser.objects.all()
    name=request.session.get('name')
    args={
        'activities': activities,
        'users': users,
        'name': name
    }
    return render(request, template_name='applied-activity.html', context=args)





def display_activity(request):
    if request.method == 'GET':
        id=request.GET.get('chance')
        print(id)
    # user = SystemUser.objects.get(user=request.user)
    # applied = SystemActivitie.objects.filter(apply_number=user)
    # applied_no = applied.apply_counter()

    activities=SystemActivitie.objects.all()

    args={
        'activities': activities,
        # 'applied_no': applied_no
    }

    return render(request, template_name='activity.html', context=args)




def create_activity(request):
    if request.method == 'POST':
        title=request.POST.get('title')   # display time added
        description=request.POST.get('description')
        duration=request.POST.get('duration')
        place=request.POST.get('place')
        requirement=request.POST.get('requirement')
        no_people=request.POST.get('no_people')
        organization=request.POST.get('organization')

        activity=SystemActivitie(
            activity_name=title,
            description=description,
            requirement=requirement,
            place=place,
            duration=duration,
            people_required=no_people,
            organization=organization,

            # time=str(datetime.now)

        )

        activity.save()
        messages.success(request, 'New jobs created !')

        # except:
        # messages.warning(request, 'New jobs not created')

        # create this page
    return render(request, template_name='create_activity.html')




def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        skill=request.POST.get('skill')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password2 != password:
            messages.warning(request, 'Passwords must match!')
            return redirect('register')

        if not '@' and '.' in email:
            messages.warning(request, 'Invalid email!')
            return redirect('register')

        filter_username=User.objects.filter(username=username)
        if filter_username:
            messages.warning(request, 'This username has already taken!')
            return redirect('register')

        sys_user=SystemUser(
            email=email,
            skill=skill,
            first_name=first_name,
            last_name=last_name
            # user=request.user

        )

        sys_user.save()

        if User:
            new_user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            new_user.save()

            user=authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('new_activity')

    return render(request, template_name='signup.html')


def login_view(request):  # not real authenticate the password
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        filter_username=User.objects.filter(username=username)
        if not filter_username:
            messages.warning(
                request, 'You dont have an account, please register!')
            return redirect('register')

        user=authenticate(
            request,
            username=username, password=password
        )

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('new_activity')

    return render(request, template_name='login.html')


def logout_view(request):
    logout(request)
    return render(request, template_name='logout.html')
