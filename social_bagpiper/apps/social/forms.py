from django import forms

from . import models


class SongForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField()
    music_sheet = forms.FileField()

    class Meta:
        model = models.Song
        fields = [
            "name",
            "description",
            "music_sheet",
        ]
