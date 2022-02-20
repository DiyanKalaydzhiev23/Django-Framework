from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pythons_auth.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )