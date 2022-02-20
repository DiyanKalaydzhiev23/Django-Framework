from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import render, redirect

from pythons_auth.forms import RegisterForm, ProfileForm, LoginForm


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        return_url = get_redirect_url(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(return_url)

    context = {
        'login_form': LoginForm(),
    }

    return render(request, 'auth/login.html', context)


@transaction.atomic
def register_view(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            my_group = Group.objects.get(name='User')
            my_group.user_set.add(user)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)

            return redirect('index')

    context = {
        'user_form': RegisterForm(),
        'profile_form': ProfileForm(),
    }

    return render(request, 'auth/register.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
