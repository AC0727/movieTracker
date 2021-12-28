from django.shortcuts import render, redirect
from .forms import AddForm, EditForm

def home(request):
    watched_list = ["Don't Look Up", "Encanto", "Spider-Man: No Way Home"]
    return render(request, 'home.html', {'watched_list': watched_list})


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

