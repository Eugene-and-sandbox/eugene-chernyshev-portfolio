from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sign_up/', sign_up, name='signup'),
    path('sign_in/', sign_in, name='signin'),
    path('sign_out/', sign_out, name='signout'),
]