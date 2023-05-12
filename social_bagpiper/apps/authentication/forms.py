from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=63)
    fullname = forms.CharField(max_length=63)
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        print("save register")
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()

        return user