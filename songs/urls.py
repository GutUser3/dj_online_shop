from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('now_date/', views.date_view),
    path('goodbye/', views.goodbye_view),
    path('song/', views.song_list_view),
    path('song_detail/<int:id>/', views.song_detail_view)
]