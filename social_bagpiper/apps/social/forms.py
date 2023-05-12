from django import forms
from . import models

class SongForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField()
    music_sheet = forms.FileField()
    
    class Meta:
        model = models.Song
        fields = ['name', 'description', 'music_sheet', ]

    # def save(self, commit=True):
    #     print("song upload save")
    #     song = super(SongForm, self).save(commit=False)
    #     if commit:
    #         song.save()

    #     return song