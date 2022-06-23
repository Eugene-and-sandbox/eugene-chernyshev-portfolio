from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('price/', price, name='price'),
    path('rules/', rules, name='rules'),
    path('guarantee/', guarantee, name='guarantee'),
    path('reviews/', reviews, name='reviews'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),

    # User account
    path('dashboard/', dashboard, name='dashboard'),
    path('toorderabox/', to_order_a_box, name='toorderabox'),
    path('delivertheparcel/', deliver_the_parcel, name='delivertheparcel'),
    path('ordershystory/', orders_hystory, name='ordershystory'),
    path('useraccountsettings/', user_account_settings, name='useraccountsettings'),
    path('myreviews/', my_reviews, name='myreviews'),
]