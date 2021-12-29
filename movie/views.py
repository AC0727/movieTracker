from django.shortcuts import render, redirect
from .forms import AddForm, EditForm
from .models import Watched

def home(request):
    queryset = Watched.objects.all()
    context = {
        "watched_list": queryset
    }
    return render(request, 'home.html', context)


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            return redirect('')

    else:
        form = AddForm()

    return render(request, 'add.html', {'form': form})


def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            return redirect('')

    else:
        form = EditForm()

    return render(request, 'edit.html', {'form': form})

