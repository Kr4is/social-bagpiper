from django import forms

from . import models


class SongForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField()
    music_sheet = forms.FileField()
    midi_file = forms.FileField(required=False, initial=None)
    mp3_file = forms.FileField(required=False, initial=None)

    class Meta:
        model = models.Song
        fields = ["name", "description", "music_sheet", "midi_file", "mp3_file"]


class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField()
    poster = forms.FileField()
    start_date = forms.DateField()
    end_date = forms.DateField()

    class Meta:
        model = models.Event
        fields = [
            "name",
            "description",
            "poster",
            "start_date",
            "end_date",
        ]
