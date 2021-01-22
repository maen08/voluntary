from .models import SystemUser
from django import forms




class SystemUserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()


    class Meta:
        model = SystemUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'skill',
            
        ]