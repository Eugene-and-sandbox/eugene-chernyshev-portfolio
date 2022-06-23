from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from accounts.admin import UserCreationForm
from accounts.forms import UserLoginForm, UserProfileUpdateForm
from portfolio.forms import ContactForm

from accounts.models import MyUser
from portfolio.models import ExamplePreviewModel, ExampleCategoryModel


def index(request):
    return render(request, 'accounts/sign-in.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signin')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign-up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio:e_examples')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/sign-in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('accounts:signin')


# @login_required(login_url='accounts:signin')
# def user_profile(request, email=None):
#     profile_info = MyUser.objects.all()
    

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             send_mail(form.cleaned_data['name'], form.cleaned_data['content'], 'eugene_chernyshev@ukr.net', ['eugene_chernyshev@ukr.net'], fail_silently=False)
#             return redirect('accounts:profile')
#     else:
#         form = ContactForm()

#     context = {
#         'title': 'Ptofile',
#         'profile_info': profile_info,
#         'form': form,
#     }
#     return render(request, 'accounts/user-profile.html', context=context)


