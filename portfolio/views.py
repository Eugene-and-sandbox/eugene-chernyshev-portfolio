from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from portfolio.models import ExamplePreviewModel

from portfolio.forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['name'], form.cleaned_data['content'], 'eugene_chernyshev@ukr.net', ['eugene_chernyshev@ukr.net'], fail_silently=False)
            return redirect('portfolio:home')
    else:
        form = ContactForm()
    return render(request, 'portfolio/index.html', {'form': form})


@login_required(login_url='accounts:signin')
def eugene_examples(request):
    examples = ExamplePreviewModel.objects.all()

    context = {
        'examples': examples,
        'title': 'Eugene portfolio site examples',    
    }

    return render(request, 'portfolio/e_examples.html', context=context)
