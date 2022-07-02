from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import generic

from shop.models import ProductModel

from shop.forms import SearchForm


# Create your views here.
def index(request, pk=None):
    products = ProductModel.objects.all()
    return render(request, 'shop/index.html', {'products': products})


def shop(request):
    return render(request, 'shop/shop.html')


def product(request, pk=None):
    result = prerender(request)
    if result:
        return result
    products = ProductModel.objects.filter(pk=pk)
    return render(request, 'shop/product-details.html', {'products': products})


def prerender(request):
    if request.GET.get('add_cart'):
        product_id = request.GET.get('add_cart')
        get_object_or_404(ProductModel, pk=product_id)
        cart_info = request.session.get('cart_info', {})
        count = cart_info.get(product_id, 0)
        count += 1
        cart_info.update({product_id: count})
        request.session['cart_info'] = cart_info
        print(cart_info)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='accounts:signin')
def cart(request):
    cart_info = request.session.get('cart_info')
    products = []
    if cart_info:
        for product.id in cart_info:
            product = get_object_or_404(ProductModel, pk=product_id)
    return render(request, 'shop/cart.html')


@login_required(login_url='accounts:signin')
def checkout(request):
    return render(request, 'shop/checkout.html')


def support(request):
    return render(request, 'shop/support.html')


@login_required(login_url='accounts:signin')
def user_profile(request):
    return render(request, 'shop/user/profile.html')


def search(request):
    search = SearchForm(request.GET)
    if search.is_valid():
        question = search.cleaned_data['question']
        products = ProductModel.objects.filter(
            Q(name__icontains=question) | Q(price__icontains=question) |
            Q(category__icontains=question)
        )

        context = {
            'products': products,
            'question': question,
        }

        return render(request, 'shop/search_results.html', context=context)
    else:
        search = SearchForm()
    return render(request, 'shop/index.html')

def handler404(request, exception):
    return render(request, 'shop/404.html', status=404)
