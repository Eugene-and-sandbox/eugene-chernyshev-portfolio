from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('', index, name='home'),
    path('users/', users_table, name='users'),
    path('customer_card/<int:pk>/', customer_card, name='customercard'),
    path('customer_card/update_info/', update_sender_info, name='updatesenderinfo'),

    path('boxorder/', box_order, name='boxorder'),
    path('deliveryparcel/', delivery_parcel, name='deliveryparcel'),
    path('history/orders/', orders_history, name='ordershistory'),
    path('history/orders/order_details/<int:pk>', order_details, name='orderdetails'),
    # path('history/returned/', returned_parcels, name='returned'),
    path('new_sender/', new_sender, name='newsender'),
    path('new_ricipient/', new_recipient, name='newrecipient'),
    path('documentation/', documentation, name='documentation'),
]
