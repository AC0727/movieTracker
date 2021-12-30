from django import forms
from .models import Movie, Watched

class SearchForm(forms.Form):
    search = forms.CharField(label='Add a movie')

class AddForm(forms.ModelForm):
    class Meta:
        model = Watched
        fields = [
            'title',
            'user_rating',
            'your_rating',
            'review',
            'date_first_watch',
            'times_watched'
        ]

class EditForm(forms.ModelForm):
    class Meta:
        model = Watched
        fields = [
            'title',
            'user_rating',
            'your_rating',
            'review',
            'date_first_watch',
            'times_watched'
        ]

