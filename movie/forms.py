from django import forms
from .models import Movie, Watched

class SearchForm(forms.Form):
    search = forms.CharField(label='Add a movie')

class AddForm(forms.ModelForm):
    class Meta:
        model = Watched
        fields = '__all__'

class EditForm(forms.ModelForm):
    class Meta:
        model = Watched
        fields = '__all__'

