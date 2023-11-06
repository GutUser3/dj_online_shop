from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models
from .forms import CreateSongForm
from .models import Song
from django.template import loader
from songs.constants import PAGINATION_LIMIT


def song_list_view(request):
    print(request.GET)
    if request.method == 'GET':
        songs = models.Song.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = songs.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)


        songs = songs[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        if search:
            songs = songs.filter(Q(title__icontains=search) | Q(artist__icontains=search))


        context_data = {
            'songs': songs,
            'user': request.user,
            'pages': range(1, max_page + 1)    }
        return render(request, 'song/song.html', context=context_data)


def song_detail_view(request, id):
    if request.method == 'GET':
        song = get_object_or_404(models.Song, id=id)

        context_data = {
            'song': song
        }
        return render(request, 'song/song_detail.html', context=context_data)


def song_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CreateSongForm,
        }

        return render(request, 'song/create.html', context=context_data)

    if not request.user.is_anonymous:

        if request.method == 'POST':
            data, files = request.POST, request.FILES
            form = CreateSongForm(data, files)

            if form.is_valid():
                cleaned_data = form.cleaned_data
                Song.objects.create(
                    album_image=cleaned_data.get('album_image'),
                    title=cleaned_data.get('title'),
                    artist=cleaned_data.get('artist'),
                    music_genre=cleaned_data.get('music_genre'),
                    cost=cleaned_data.get('cost')
                )
                return redirect('/song/')

            return render(request, 'song/create.html', context={'form': form})

    else:
        return HttpResponse('Error. You should be logged in to add songs.')
