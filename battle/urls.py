from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('review/<int:pk>', day_review, name='review'),
    path('photo/', photo, name='photo'),
    path('video/', video, name='video'),
    path('audio/', audio, name='audio'),
    path('articles/', articles, name='articles'),
    path('event/<int:pk>', current_event, name='event'),
    path('daylist/', day_list, name='daylist'),
    path('about/', about, name='about'),
    path('contact/', contacts, name='contacts'),
]
