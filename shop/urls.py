from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('product/<int:pk>/', product, name='product-details'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('profile/', user_profile, name='user-profile'),
    path('support/', support, name='support'),
    path('search/', search, name='search'),
]
