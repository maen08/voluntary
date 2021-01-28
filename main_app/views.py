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
from hitcount.models import HitCount
from hitcount.views import HitCountMixin, HitCountDetailView




# def onbuild_page(request):
#     return render(request, template_name='build.html')



# class ApplyLogicView(HitCountDetailView):
#     model = SystemActivitie
#     template_name = 'activity.html'
#     count_hit = True
#      # the primary key for the hitcount object #}
#     {{hitcount.pk}}

#          # the total hits for the object #}
#     {{hitcount.total_hits}}





def apply_view(request, activity_id):
    get_activity = get_object_or_404(SystemActivitie, pk=activity_id)
    applied_people = get_activity.apply_number.add(request.user)   # just save in DB the user who applied

    # messages.success(request, 'Success, Activity added!')
    return redirect('new_activity')

    # print(type(applied_people))

    # if get_activity.people_required < int(applied_people):
    #     print('NO ROOM FOR THIS')
    #     messages.warning(request, 'Sorry, no chance for now!')


    # # request.session['people_chances'] = no_people
    # # request.session['people_applied'] = get_activity.apply_number.add(request.user)

    # else:
    #     messages.success(request, 'Success, Activity added!')
    #     return redirect('new_activity')

   



def applied_activity(request):
    activities = SystemActivitie.objects.all()
    users = SystemUser.objects.all()
    args = {
        'activities': activities,
        'users': users
        
    }
    return render(request, template_name='applied-activity.html', context=args)


def display_activity(request):
    # people_chances = request.session.get('people_chances')
    # people_applied = request.session.get('people_applied')

    # total_people = people_chances.apply_counter()

    # if total_people >= people_applied:
    #     print('NO ROOM FOR THIS')
    #     messages.warning(request, 'Sorry, no chance for now!')

    applied = get_object_or_404(SystemActivitie)
    applied_no = applied.apply_counter()
    activities = SystemActivitie.objects.all()

    args = {
        'activities': activities,
        'applied_no': applied_no
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


def login_view(request):  # not real authenticate the password
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        filter_username = User.objects.filter(username=username)
        if not filter_username:
            messages.warning(
                request, 'You dont have an account, please register!')
            return redirect('register')

        user = authenticate(
            request,
            username=username, password=password
        )

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('new_activity')

    return render(request, template_name='login.html')


def logout_view(request):
    logout(request)
    return render(request, template_name='logout.html')
