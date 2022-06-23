from django import template
from django.core.mail import send_mail
from django.shortcuts import redirect

from portfolio.forms import ContactForm

from crm_employees.models import *

register = template.Library()


@register.simple_tag()
def side_panel_form(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                send_mail(form.cleaned_data['name'], form.cleaned_data['content'], 'eugene_chernyshev@ukr.net', ['eugene_chernyshev@ukr.net'], fail_silently=False)
                return redirect('portfolio:home')
    else:
        form = ContactForm()
