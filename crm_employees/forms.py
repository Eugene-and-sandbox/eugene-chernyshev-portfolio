from cProfile import label
import email
from turtle import width
from django import forms

from crm_employees.models import CustomerRecipientInfoModel, BoxOrderModel, \
DeliveryTariffModel, CustomerDiscountModel, CourierTariffModel
from accounts.models import MyUser


class UpdateUserInfoForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))


class BoxOrderForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=MyUser.objects.all(), label='', empty_label='Choose sender', widget=forms.Select(attrs={'class': 'form-control w-75'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    size_ten = forms.IntegerField(label='10', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75', 'min': 0, 'placeholder': 'Box of 10 kg'}))
    size_twenty = forms.IntegerField(label='20', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75', 'min': 0, 'placeholder': 'Box of 20 kg'}))
    size_thirty = forms.IntegerField(label='30', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75', 'min': 0, 'placeholder': 'Box of 30 kg'}))


class DeliveryParcelForm(forms.Form):
    sender = forms.ModelChoiceField(queryset=MyUser.objects.all(), label='', empty_label='Senders', widget=forms.Select(attrs={'class': 'form-control w-75'}))
    recipient = forms.ModelChoiceField(queryset=CustomerRecipientInfoModel.objects.all(), label='', empty_label='Recipients', widget=forms.Select(attrs={'class': 'form-control mt-3 w-75'}))
    weight = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75'}))
    width = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75'}))
    height = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75'}))
    length = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control mt-3 w-75'}))
    price = forms.ModelChoiceField(queryset=DeliveryTariffModel.objects.all(), label='', empty_label='Tariff', widget=forms.Select(attrs={'class': 'form-control mt-3 w-75'}))
    discount = forms.ModelChoiceField(queryset=CustomerDiscountModel.objects.all(), label='', empty_label='Discount', widget=forms.Select(attrs={'class': 'form-control mt-3 w-75'}))
    courier = forms.ModelChoiceField(queryset=CourierTariffModel.objects.all(), label='', empty_label='Courier', widget=forms.Select(attrs={'class': 'form-control mt-3 w-75'}))


class AddNewRecipientForm(forms.Form):
    parent_sender = forms.ModelChoiceField(queryset=MyUser.objects.all(), label='', empty_label='Choose sender', widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    surname = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.CharField(label='', required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))