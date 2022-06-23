from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('examples_by_eugene/', eugene_examples, name='e_examples'),
]