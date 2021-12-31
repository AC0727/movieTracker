from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add/<int:movie_id>/', views.add, name="add"),
    path('edit/<int:movie_id>/', views.add, name="edit"),
    path('search/', views.search, name="search"),
    path('page/<int:movie_id>/', views.page, name="page"),
]