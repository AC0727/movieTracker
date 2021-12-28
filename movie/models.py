from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    #genre =
    user_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title





