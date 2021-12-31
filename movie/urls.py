from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('add/<int:movie_id>/', views.add),
    path('edit/<int:movie_id>/', views.add),
    path('search/', views.search),
    path('page/<int:movie_id>/', views.page),
]