from django import forms
from .models import Movie, Watched

class SearchForm(forms.Form):
    search = forms.CharField(label='Add a movie')

class AddForm(forms.ModelForm):
    class Meta:
        model = Watched
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['title'].widget.attrs["readonly"] = True

        self.fields['user_rating'].disabled = True
        self.fields['user_rating'].widget.attrs["readonly"] = True

class EditForm(forms.ModelForm):
    class Meta:
        model = Watched
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['title'].widget.attrs["readonly"] = True

        self.fields['user_rating'].disabled = True
        self.fields['user_rating'].widget.attrs["readonly"] = True

