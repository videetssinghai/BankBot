from django import forms
from .models import User



class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'FirstName',
            'LastName',
            'Email',
            'Password',

        ]