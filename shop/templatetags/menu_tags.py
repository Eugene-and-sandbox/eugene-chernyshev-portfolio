from django import template
from shop.models import MenuTagModel

register = template.Library()


@register.simple_tag()
def get_menu_links():
    return MenuTagModel.objects.all()
