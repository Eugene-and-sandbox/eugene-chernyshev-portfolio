from collections import defaultdict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import MyUser
from crm_employees.models import DeliveryParcelModel, BoxOrderModel

from crm_employees.views import BoxOrderForm


def index(request):
    return render(request, 'crm_customers/index.html')


def price(request):
    return render(request, 'crm_customers/index.html')


def rules(request):
    return render(request, 'crm_customers/rules.html')


def guarantee(request):
    return render(request, 'crm_customers/guarantee.html')


def reviews(request):
    return render(request, 'crm_customers/reviews.html')


def contacts(request):
    return render(request, 'crm_customers/contacts.html')


def about(request):
    return render(request, 'crm_customers/about.html')


@login_required(login_url='accounts:signin')
def dashboard(request):
    return render(request, 'crm_customers/user_account/dashboard.html')


@login_required(login_url='accounts:signin')
def to_order_a_box(request):
    initial = {
        'email': request.user,
    }
    if request.method == 'POST':
        form = BoxOrderForm(request.POST, initial='email')
        if form.is_valid():
            BoxOrderModel.objects.create(**form.cleaned_data)
            return redirect('ordershystory')
    else:
        form = BoxOrderForm()
    return render(request, 'crm_customers/user_account/to_order_a_box.html', {'form': form})


@login_required(login_url='accounts:signin')
def deliver_the_parcel(request):
    return render(request, 'crm_customers/user_account/deliver_the_parcel.html')


@login_required(login_url='accounts:signin')
def orders_hystory(request):
    user_deliveries = DeliveryParcelModel.objects.filter(email__exact=request.user.email)
    user_boxes = BoxOrderModel.objects.filter(email__exact=request.user.email)

    context = {
        'user_deliveries': user_deliveries,
        'user_boxes': user_boxes,
    }
    return render(request, 'crm_customers/user_account/orders_hystory.html', context=context)


@login_required(login_url='accounts:signin')
def user_account_settings(request):
    account_info = MyUser.objects.filter(email__exact=request.user.email)

    context = {
        'account_info': account_info,
    }

    return render(request, 'crm_customers/user_account/user_account_settings.html', context=context)


@login_required(login_url='accounts:signin')
def my_reviews(request):
    return render(request, 'crm_customers/user_account/my_reviews.html')