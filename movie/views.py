from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import add_form, search_form
from .models import Watched, Movie

def home(request):
    queryset = Watched.objects.all()
    context = {
        "watched_list": queryset,
        "search_form": search_form()
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
        'search_form': search_form(),
    })


def search(request):
    if request.method == 'POST':
        form = search_form(request.POST)

        if form.is_valid():
            movie = Movie()
            return render(request, 'search.html', {
                'search_form': form,
                'results': movie.search(form.cleaned_data['search']),
                'search_query': form.cleaned_data['search']
            })

    else:
        form = search_form()

    return render(request, 'search.html', { 'search_form': form })


def add(request, imdb_id):
    movie = Movie().get_media(imdb_id)

    try:
        rating = movie.data['rating']
    except:
        rating = 0

    form = add_form(request.POST or None, initial={
        'title': movie,
        'user_rating': float(rating)}) #prefilled these fields
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/') #go back to home screen
    return render(request, 'add.html', {
         'form': form,
         'movie': movie,
         'img_src': movie['full-size cover url'],
         'search_form': search_form(),
         })


def edit(request, movie_id): #don't think I'll need edit.html
    obj = get_object_or_404(Watched, id=movie_id)
    movie = Movie().get_media(movie_id) #wrong movie id
    form = add_form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'add.html', {
        'form': form,
        'movie': movie,
        'img_src': movie['full-size cover url'],
        'search_form': search_form(),
        })


def delete(request, movie_id):
    obj = get_object_or_404(Watched, id=movie_id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('/')
    context = {
        "movie": obj
    }
    return render(request, 'delete.html', context)


def to_watch(request):
    return render(request, 'to_watch.html', {'search_form': search_form(),})

