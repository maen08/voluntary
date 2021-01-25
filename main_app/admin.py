from django.contrib import admin
from django.contrib.auth.models import Group
from .models import SystemUser, SystemActivitie


admin.site.register(SystemUser)
admin.site.register(SystemActivitie)


admin.site.unregister(Group)
admin.site.site_header = "VMS Administration"