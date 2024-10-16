from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'release_date', 'poster']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
