from django import forms
from .models import Movie, Watched

class search_form(forms.Form):
    search = forms.CharField(
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'search movies, shows, etc.'})
    )


class add_form(forms.ModelForm):
    class Meta:
        model = Watched
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['title'].widget.attrs["readonly"] = True

        self.fields['user_rating'].disabled = True
        self.fields['user_rating'].widget.attrs["readonly"] = True



