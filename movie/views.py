from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddForm, SearchForm
from .models import Watched, Movie

def home(request):
    queryset = Watched.objects.all()
    context = {
        "watched_list": queryset,
        "search_form": SearchForm()
    }
    return render(request, 'home.html', context)


def page(request, movie_id):
    movie = Movie().get_media(movie_id)
    if movie:
        cast = movie['cast']
        del cast[20:]

    return render(request, 'page.html', {
        'movie': movie,
        'cast': cast,
        'img_src': movie['full-size cover url'],
    })


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            movie = Movie()
            return render(request, 'search.html', {
                'search_form': form,
                'results': movie.search(form.cleaned_data['search']),
                'search_query': form.cleaned_data['search']
            })

    else:
        form = SearchForm()

    return render(request, 'search.html', { 'search_form': form })


def add(request, movie_id):
    movie = Movie().get_media(movie_id)
    form = AddForm(request.POST or None, initial={
        'title': movie,
        'user_rating': float(movie.data['rating'])}) #prefilled these fields
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/') #go back to home screen
    return render(request, 'add.html', {
         'form': form,
         'movie': movie,
         'img_src': movie['full-size cover url']})


def edit(request, movie_id): #don't think I'll need edit.html
    obj = get_object_or_404(Watched, id=movie_id)
    movie = Movie().get_media(movie_id) #wrong movie id
    form = AddForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'add.html', {
        'form': form,
        'movie': movie,
        'img_src': movie['full-size cover url']})
