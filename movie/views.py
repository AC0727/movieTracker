from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import AddForm, EditForm, SearchForm
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
    # if request.method == 'POST':
    #     form = AddForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         movie = Watched()
    #         return render(request, 'add.html', {
    #             'form': form,
    #             'results': movie.search(form.cleaned_data['search']),
    #             'search_query': form.cleaned_data['search']
    #         })
    #
    # else:
    #     movie = Watched().get_media(movie_id)
    #     form = AddForm()
    #
    #     return render(request, 'add.html', {
    #         'form': form,
    #         'movie': movie,
    #         'img_src': movie['full-size cover url']})
    movie = Movie().get_media(movie_id)
    form = AddForm(request.POST or None, initial={
        'title': movie,
        'user_rating': float(movie.data['rating'])})
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'add.html', {
         'form': form,
         'movie': movie,
         'img_src': movie['full-size cover url']})


def edit(request, movie_id):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        movie = Watched().get_media(movie_id)
        form = EditForm()

        return render(request, 'edit.html', {
            'form': form,
            'movie': movie,
            'img_src': movie['full-size cover url']})

