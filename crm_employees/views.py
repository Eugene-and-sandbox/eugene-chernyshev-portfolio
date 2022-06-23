from datetime import date, datetime
from multiprocessing import context
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from pkg_resources import require

from accounts.admin import UserCreationForm
from crm_employees.forms import UpdateUserInfoForm, BoxOrderForm, DeliveryParcelForm, AddNewRecipientForm
from portfolio.forms import ContactForm

from accounts.models import MyUser
from crm_employees.models import BoxOrderModel, DeliveryParcelModel, CustomerRecipientInfoModel


@login_required(login_url='accounts:signin')
def index(request):
    parcels_count = DeliveryParcelModel.objects.filter().count()
    boxes_count = BoxOrderModel.objects.filter().count()
    customers_count = MyUser.objects.filter().count()

    last_boxes = BoxOrderModel.objects.order_by('-ordering_date')[:5]
    last_boxes_paginator = Paginator(last_boxes, 4)
    last_boxes_number = request.GET.get('page')
    last_boxes_numbers = last_boxes_paginator.get_page(last_boxes_number)

    last_deliveries = DeliveryParcelModel.objects.order_by('-ordering_date')[:5]
    last_deliveries_paginator = Paginator(last_deliveries, 5)
    last_deliveries_number = request.GET.get('page')
    last_deliveries_obj = last_deliveries_paginator.get_page(last_deliveries_number)

    context = {
        'title': 'Dashboard',
        'parcels_count': parcels_count,
        'boxes_count': boxes_count,
        'customers_count': customers_count,
        'last_boxes_numbers': last_boxes_numbers,
        'last_deliveries_obj': last_deliveries_obj,
    }

    return render(request, 'crm_employees/dashboard.html', context=context)


@login_required(login_url='accounts:signin')
def users_table(request):
    users = MyUser.objects.all()
    context = {
        'users': users,
        'title': 'Users table',
    }
    return render(request, 'crm_employees/users.html', context=context)


@login_required(login_url='accounts:signin')
def customer_card(request, pk=None):
    customer_info = MyUser.objects.filter(pk=pk)
    customer_orders = DeliveryParcelModel.objects.filter(email__exact=request.user.email)
    customer_orders_pagination = Paginator(customer_orders, 3)
    customer_orders_nums = request.GET.get('page')
    customer_orders_obj = customer_orders_pagination.get_page(customer_orders_nums)

    context = {
        'customer_info': customer_info,
        'customer_orders': customer_orders,
        'customer_orders_obj': customer_orders_obj,
    }

    return render(request, 'crm_employees/customer_card.html', context=context)

@login_required(login_url='accounts:signin')
def profile(request):
    profile_info = MyUser.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['name'], form.cleaned_data['content'], 'eugene_chernyshev@ukr.net', ['eugene_chernyshev@ukr.net'], fail_silently=False)
            return redirect('accounts:profile')
    else:
        form = ContactForm()

    context = {
        'title': 'Employee profile',
        'profile_info': profile_info,
        'form': form,
    }
    return render(request, 'crm_employees/profile.html', context=context)


@login_required(login_url='accounts:signin')
def update_sender_info(request, pk=None):
    user = request.user
    if request.method == 'POST':
        update_user_form = UpdateUserInfoForm(request.POST, initial={
                    'email': user.email, 
                    'name': user.name, 
                    'surname': user.surname,
                    'phone': user.phone,
                    'address': user.address
                })
        if update_user_form.is_valid():      
            update_user_form.save()
            return redirect('crm_employees:profile')
    else:
        update_user_form = UpdateUserInfoForm()
    return render(request, 'crm_employees/updates/sender_info_update.html', {'update_user_form': update_user_form})
        


@login_required(login_url='accounts:signin')
def box_order(request):
    if request.method == 'POST':
        form = BoxOrderForm(request.POST)
        if form.is_valid():
            BoxOrderModel.objects.create(**form.cleaned_data)
            messages.success(request, 'Order has been saved')
            return redirect('crm_employees:boxorder')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = BoxOrderForm()
    return render(request, 'crm_employees/box_order.html', {'form': form, 'title': 'Order a Box'})


@login_required(login_url='accounts:signin')
def delivery_parcel(request):
    if request.method == 'POST':
        form = DeliveryParcelForm(request.POST)
        if form.is_valid():
            DeliveryParcelModel.objects.create(**form.cleaned_data)
            messages.success(request, 'Order saved')
            return redirect('crm_employees:deliveryparcel')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = DeliveryParcelForm()
    return render(request, 'crm_employees/delivery_parcel.html', {'form': form, 'title': 'Delivery Parcel'})


@login_required(login_url='accounts:signin')
def orders_history(request):
    user_photo = MyUser.objects.all()

    box_orders = BoxOrderModel.objects.order_by('-ordering_date')
    box_orders_pagination = Paginator(box_orders, 20)
    box_order_number = request.GET.get('page')
    box_order_obj = box_orders_pagination.get_page(box_order_number)

    delivery_orders = DeliveryParcelModel.objects.order_by('-ordering_date')
    delivery_orders_pagination = Paginator(delivery_orders, 20)
    delivery_orders_number = request.GET.get('page')
    delivery_orders_obj = delivery_orders_pagination.get_page(delivery_orders_number)

    context = {
        'title': 'Orders history',
        'box_order_obj': box_order_obj,
        'delivery_orders': delivery_orders,
        'delivery_orders_obj': delivery_orders_obj,
        'user_photo': user_photo,
    }
    return render(request, 'crm_employees/orders_history.html', context=context)


@login_required(login_url='accounts:signin')
def order_details(request, pk=None):
    box_details = BoxOrderModel.objects.filter(pk=pk)
    delivery_details = DeliveryParcelModel.objects.filter(pk=pk)

    context = {
        'box_details': box_details,
        'delivery_details': delivery_details,
        'title': 'Order Details',
    }

    return render(request, 'crm_employees/order_details.html', context=context)


@login_required(login_url='accounts:signin')
def returned_parcels(request):
    return render(request, 'crm_employees/returned_parcels.html', {'title': 'Returned Parcels'})


@login_required(login_url='accounts:signin')
def new_sender(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'crm_employees/new_sender.html', {'form': form, 'title': 'Add new sender'})


@login_required(login_url='accounts:signin')
def new_recipient(request):
    if request.method == 'POST':
        form = AddNewRecipientForm(request.POST)
        if form.is_valid():
            CustomerRecipientInfoModel.objects.create(**form.cleaned_data)
            return redirect('crm_employees:newrecipient')
    else:
        form = AddNewRecipientForm()
    return render(request, 'crm_employees/new_recipient.html', {'form': form, 'title': 'Add new recipient'})


def documentation(request):
    return render(request, 'crm_employees/documentation.html', {'title': 'Documentation'})


def handler404(request, exception):
    return render(request, 'crm_employees/404.html', status=404)
