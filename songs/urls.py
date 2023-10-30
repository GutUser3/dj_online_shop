from django.urls import path
from . import views

urlpatterns = [
    path('song/', views.song_list_view),
    path('song_detail/<int:id>/', views.song_detail_view),
    path('song/create/', views.song_create_view)
]