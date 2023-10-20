from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloView),
    path('now_date/', views.dateView),
    path('goodbye/', views.goodbyeView),
    path('song/', views.songListView)
]