from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Add a movie')

class AddForm(forms.Form):
    rating = forms.DecimalField(label='Rating')
    date = forms.DateField(label='Date')
    review = forms.CharField(label='Review')

class EditForm(forms.Form):
    rating = forms.DecimalField(label='Rating')
    date = forms.DateField(label='Date')
    review = forms.CharField(label='Review')

