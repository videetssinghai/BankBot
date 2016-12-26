from django import forms
from .models import User



class UserForm(forms.ModelForm):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    Email = forms.EmailField()
    Password = forms.PasswordInput()

    class Meta:
        model = User
        fields = [
            'FirstName',
            'LastName',
            'Email',
            'Password',

        ]




class LoginForm (forms.ModelForm):
    Email = forms.EmailField()
    Password = forms.PasswordInput()

    class Meta:

        model = User
        fields = {
            'Email',
            'Password'


        }