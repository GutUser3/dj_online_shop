from django.db import models

class Songs(models.Model):

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    SONG_GENRE = (
        ("Поп", "Поп"),
        ("EDM", "EDM"),
        ("J-Pop", "J-Pop"),
        ("R&B", "R&B"),
    )

    title = models.CharField(max_length=100, verbose_name='Название песни', null=True)
    album_image = models.ImageField(upload_to='', verbose_name='Картинка альбома', null=True)
    music_genre = models.CharField(max_length=100, choices=SONG_GENRE, verbose_name='Жанр песни', null=True)
    cost = models.PositiveIntegerField(verbose_name='Укажите цену песни', null=True)
    singer = models.CharField(max_length=100, verbose_name='Укажите имя исполнителя', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
