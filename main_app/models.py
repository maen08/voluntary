from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class SystemUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # user = models.ForeignKey(User,
    #  on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill
    


class SystemActivitie(models.Model):
    activity_name = models.CharField(max_length=100)
    description = models.TextField()
    requirement = models.TextField()
    place = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    duration = models.IntegerField()
    people_required = models.IntegerField()    
    organization = models.CharField(max_length=100)
    apply_number = models.ManyToManyField(User)


    def apply_counter(self):
        return self.apply_number.count()

    def __str__(self):
        return self.activity_name
    