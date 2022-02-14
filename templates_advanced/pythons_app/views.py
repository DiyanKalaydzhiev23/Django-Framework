from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.decorators import groups_required
from .forms import PythonCreateForm
from .models import Python


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


@groups_required(['User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')


def sign_in(request):
    user = authenticate(username="pesho", password="qwertypesho")

    if user:
        login(request, user)
        return redirect('index')

    return HttpResponse("User doesn't exist")


def logout_view(request):
    logout(request)
    return redirect('index')
