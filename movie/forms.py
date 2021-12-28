from django import forms

class AddForm(forms.Form):
    title = forms.CharField(label='Title')
    genre = forms.CharField(label='Genre')
    rating = forms.CharField(label='Rating')
    date = forms.DateField(label='Date')
    review = forms.CharField(label='Review')

class EditForm(forms.Form):
    title = forms.CharField(label='Title')
    genre = forms.CharField(label='Genre')
    rating = forms.CharField(label='Rating')
    date = forms.DateField(label='Date')
    review = forms.CharField(label='Review')

