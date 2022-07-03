from shop.forms import SearchForm
from shop.models import ProductModel

def add_default_data(request):
    search_form = SearchForm()
    count_in_cart = 0
    sum_in_cart = 0
    cart_info = request.session.get('cart_info', {})
    for key in cart_info:
        count_in_cart += cart_info[key]
        sum_product = ProductModel.objects.get(pk=key).price * cart_info[key]
        sum_in_cart += sum_product

    return {
        'search_form': search_form,
        'count_in_cart': count_in_cart,
        'sum_in_cart': sum_in_cart,
        }
