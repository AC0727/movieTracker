from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, blank=False)
    user_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title

class Watched(Movie):
    your_rating = models.DecimalField(max_digits=3, decimal_places=1)
    review = models.TextField(blank=True)
    date_first_watch = models.DateField()
    times_watched = models.IntegerField(blank=False)

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)




