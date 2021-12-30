from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search')

class AddForm(forms.Form):
    rating = forms.CharField(label='Rating')
    date = forms.DateField(label='Date')
    review = forms.CharField(label='Review')

class EditForm(forms.Form):
    rating = forms.CharField(label='Rating')
    date = forms.DateField(label='Date')
    review = forms.CharField(label='Review')

