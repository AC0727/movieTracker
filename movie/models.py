from django.db import models
from imdb import IMDb



class Movie(models.Model):
    title = models.CharField(max_length=200, blank=False)
    user_rating = models.DecimalField(max_digits=3, decimal_places=1)
    imdb_id = models.IntegerField(null=True, editable=False)

    def __str__(self):
        return self.title

    def search(self, keyword):
        ia = IMDb()
        search = ia.search_movie(keyword)
        results = {}
        
        for j in search:
            i = j.movieID
            results[i] = {}
            results[i]['title'] = j['title']
            try:
                results[i]['year'] = j['year']
            except KeyError:
                results[i]['year'] = ['???']
            results[i]['cover']=j['full-size cover url']

        return results
    
    def get_media(self, id):
        ia = IMDb()
        return ia.get_movie(id)


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




