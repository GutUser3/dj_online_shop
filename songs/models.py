from django.db import models
from songs.constants import SONG_GENRE

class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Song(models.Model):
    """ References """
    hashtags = models.ManyToManyField(Hashtag)

    """ Base Fields """
    title = models.CharField(max_length=100, verbose_name='Название песни', null=True)
    album_image = models.ImageField(verbose_name='Картинка альбома', null=True)
    music_genre = models.CharField(max_length=100, choices=SONG_GENRE, verbose_name='Жанр песни', null=True)
    cost = models.PositiveIntegerField(verbose_name='Укажите цену песни', null=True)
    artist = models.CharField(max_length=100, verbose_name='Укажите имя исполнителя', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'