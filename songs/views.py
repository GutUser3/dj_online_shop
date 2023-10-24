from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

# Less code way

def song_list_view(request):
    if request.method == 'GET':
        song_value = models.Song.objects.all()

        context_data = {
            'song_key': song_value
        }
        return render(request, 'song/song.html', context=context_data)

def song_detail_view(request, id):
    if request.method == 'GET':
        song_id = get_object_or_404(models.Song, id=id)

        context_data = {
            'song_id': song_id
        }
        return render(request, 'song/song_detail.html', context=context_data)

# More code way

# def postListView(request):
#     post_value = models.Post.objects.all()
#     html_filename = 'song/song.html'
#     context = {
#         'post_key': post_value,
#     }
#     return render(request, html_filename, context)





def hello_view(request):
    return HttpResponse("<h1>Hello! It's my project</h1>")

def date_view(request):
    return HttpResponse(f'<h1>{datetime.now().date()}</h1>')

def goodbye_view(request):
    return HttpResponse('<h1>Goodbye user!</h1>')