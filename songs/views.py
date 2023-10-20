from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models

# Less code way

def songListView(request):
    song_value = models.Songs.objects.all()
    return render(request, 'song/song.html', {'song_key': song_value})


# More code way

# def postListView(request):
#     post_value = models.Post.objects.all()
#     html_filename = 'song/song.html'
#     context = {
#         'post_key': post_value,
#     }
#     return render(request, html_filename, context)





def helloView(request):
    return HttpResponse("<h1>Hello! It's my project</h1>")

def dateView(request):
    return HttpResponse(f'<h1>{datetime.now().date()}</h1>')

def goodbyeView(request):
    return HttpResponse('<h1>Goodbye user!</h1>')