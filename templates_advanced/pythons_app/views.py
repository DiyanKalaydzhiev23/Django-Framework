from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


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
