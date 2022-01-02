from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add/<int:imdb_id>/', views.add, name="movie-add"),
    path('edit/<int:movie_id>/', views.edit, name="movie-edit"),
    path('search/', views.search, name="search"),
    path('page/<int:movie_id>/', views.page, name="movie-page"),
    path('delete/<int:movie_id>/', views.delete, name="movie-delete"),
    path('to_watch/', views.to_watch, name="to-watch")
]
