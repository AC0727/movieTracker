from django.contrib import admin

# Register your models here.
from .models import Movie, Watched, Genre

admin.site.register(Movie)
admin.site.register(Watched)
admin.site.register(Genre)

