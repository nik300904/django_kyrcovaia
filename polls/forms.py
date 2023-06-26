from django import forms
from .models import *


class SearchFilmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["rating"].widget.attrs.update({"type": "text"})

    class Meta:
        model = Films
        # fields = ['genres', 'release_film', 'rating', 'actors', 'director', 'country']
        fields = ['country', 'genres', 'rating', 'release_film', 'actors']
        widgets = {
            'rating': forms.NumberInput(attrs={'value': 0})
        }
