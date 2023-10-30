from django import forms
from songs import constants


class CreateSongForm(forms.Form):
    album_image = forms.FileField()
    title = forms.CharField(min_length=2, max_length=64)
    artist = forms.CharField()  # widget=forms.Textarea()
    music_genre = forms.ChoiceField(choices=constants.SONG_GENRE)
    cost = forms.IntegerField(required=False, min_value=0)