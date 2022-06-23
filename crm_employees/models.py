from decimal import Decimal
from distutils.command import upload
import numbers
from pyexpat import model
from statistics import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.forms import Textarea

from accounts.models import MyUser

import random


class CustomerRecipientInfoModel(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    parent_sender = models.ForeignKey(MyUser, db_index=True, on_delete=models.CASCADE, related_name='recipient_relation', verbose_name='Sender')

    def __str__(self):
        return f'{self.name} {self.surname} - sender: {self.parent_sender.name} {self.parent_sender.surname}, {self.address}, {self.phone}'

    class Meta:
        ordering = ['parent_sender']
        verbose_name = 'recipient info'
        verbose_name_plural = 'Recipients info'


class BoxOrderModel(models.Model):
    customer = models.ForeignKey(MyUser, db_index=True, on_delete=models.PROTECT)
    email = models.EmailField()
    size_ten = models.IntegerField(blank=True, default='0', verbose_name='10', help_text='Count of boxes')
    size_twenty = models.IntegerField(blank=True, default='0', verbose_name='20', help_text='Count of boxes')
    size_thirty = models.IntegerField(blank=True, default='0', verbose_name='30', help_text='Count of boxes')
    price = models.IntegerField()
    ordering_date = models.DateTimeField(auto_now_add=True)
    STATUS = [
        ('NEW', 'New order'),
        ('DEL', 'Delivered'),
    ]
    status = models.CharField(choices=STATUS, max_length=3, default='NEW')
    completed_at = models.DateTimeField(auto_now=False, blank=True, null=True)

    def total_amount(self):
        amount = 0
        amount += (self.size_ten + self.size_twenty + self.size_thirty) * 20

        return f'{amount}$'

    def __str__(self):
        return f'{self.size_ten}, {self.size_twenty}, {self.size_thirty}'
    
    class Meta:
        verbose_name = 'box order'
        verbose_name_plural = 'Boxes orders'


def intarnationsal_track_number_generator():
    number = random.randint(1, 100000)
    track_number = 'UA0187' + str(number) + 'TL'
    return track_number

def inside_track_number_generator():
    number = random.randint(1, 100000000)
    return number


class DeliveryParcelModel(models.Model):
    sender = models.ForeignKey(MyUser, db_index=True, on_delete=models.PROTECT)
    email = models.EmailField()
    recipient = models.ForeignKey(CustomerRecipientInfoModel, db_index=True, on_delete=models.PROTECT)
    weight = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.ForeignKey('DeliveryTariffModel', db_index=True, on_delete=models.PROTECT)
    discount = models.ForeignKey('CustomerDiscountModel', db_index=True, on_delete=models.PROTECT, default=1)
    courier = models.ForeignKey('CourierTariffModel', db_index=True, on_delete=models.PROTECT, default=3)
    ordering_date = models.DateTimeField(auto_now_add=True)
    intarnational_track_number = models.CharField(max_length=13, default=intarnationsal_track_number_generator, unique=True)
    inside_track_number = models.CharField(max_length=8, default=inside_track_number_generator, unique=True)
    STATUSES = [
        ('NEW', 'New parcel'),
        ('TBC', 'Took by courier'),
        ('SCW', 'S.C.Warehouse'),
        ('TRP', 'Transporting'),
        ('COS', 'Customer Service'),
        ('DEL', 'going to recipient'),
        ('COM', 'Completed'),
        ('RET', 'Returned')
    ]
    status = models.CharField(choices=STATUSES, max_length=3, default='NEW')
    completed_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    receipt = models.ImageField(upload_to='media/images/receipts', blank=True, null=True)
    invoice = models.ImageField(upload_to='media/images/invoices', blank=True, null=True)

    def delivery_amount(self):
        amount = 0
        amount += self.price.price * self.weight

        if self.discount:
            amount = round(amount * Decimal(1 - self.discount.value / 100))

        return '{0}$'.format(amount)
    delivery_amount.short_description = 'Order amount'

    def total_amount(self):
        amount_start = 0
        amount_start += self.price.price * self.weight

        if self.discount:
            amount_start = round(amount_start * Decimal(1 - self.discount.value / 100))

        amount_finish = amount_start + self.courier.price
        return '{0}$'.format(amount_finish)

    def __str__(self):
        return f'{self.sender.name} {self.sender.surname}'

    class Meta:
        verbose_name = 'delivery order'
        verbose_name_plural = 'Delivery orders'


class BoxTariffModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return '{0}: {1}$'.format(self.name, self.price)

    class Meta:
        verbose_name = 'box tariff'
        verbose_name_plural = 'Tariff: Boxes'


class DeliveryTariffModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return '{0}: {1}$'.format(self.name, self.price)

    class Meta:
        verbose_name = 'delivery tariff'
        verbose_name_plural = 'Tariff: Delivery'


class CourierTariffModel(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()

    def __str__(self):
        return '{0}: {1}$'.format(self.name, self.price)

    class Meta:
        verbose_name = 'courier tariff'
        verbose_name_plural = 'Tariff: Courier'


class CustomerDiscountModel(models.Model):
    code = models.CharField(max_length=13)
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return '{0}: {1}%'.format(self.code, self.value)

    class Meta:
        verbose_name = 'discount value'
        verbose_name_plural = 'Tariff: Discount'