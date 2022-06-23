from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from battle.models import GeneralDayDescriptionModel, LostItemsListModel, DayEventModel, DayPhotoModel, DayVideoModel, DayAudioModel, DayArticleModel
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    current_day = GeneralDayDescriptionModel.objects.order_by('-pk').first()

    day_review = GeneralDayDescriptionModel.objects.all()
    day_review_paginator = Paginator(day_review, 3)
    day_review_page_number = request.GET.get('page')
    day_review_page_obj = day_review_paginator.get_page(day_review_page_number)

    photos = DayPhotoModel.objects.order_by('-parent')
    photos_paginator = Paginator(photos, 6)
    photos_page_number = request.GET.get('page')
    photos_page_obj = photos_paginator.get_page(photos_page_number)

    videos = DayVideoModel.objects.order_by('-parent')
    videos_paginator = Paginator(videos, 4)
    videos_page_number = request.GET.get('page')
    videos_page_obj = videos_paginator.get_page(videos_page_number)

    lost_items = LostItemsListModel.objects.all().order_by('-date')

    context = {
        'current_day': current_day,
        'day_review_page_obj': day_review_page_obj,
        'photos_page_obj': photos_page_obj,
        'videos': videos,
        'lost_items': lost_items,
    }

    return render(request, 'battle/index.html', context=context)


def day_review(request, pk=None):
    events = DayEventModel.objects.filter(day=pk).order_by('event_time')

    context = {
        'title': 'Огляд дня',
        'events': events,
    }
    return render(request, 'battle/day_review.html', context=context)


def photo(request):
    photos = DayPhotoModel.objects.all()
    return render(request, 'battle/photos.html', {'photos': photos})


def video(request):
    videos = DayVideoModel.objects.all()
    return render(request, 'battle/videos.html', {'videos': videos})


def audio(request):
    audios = DayAudioModel.objects.all()
    return render(request, 'battle/audios.html', {'audios': audios})


def current_event(request, pk=None):
    description = DayEventModel.objects.filter(pk=pk)
    # description = DayEventModel.objects.all()
    # photos = DayPhotoModel.objects.order_by('-parent')[0]
    # videos = DayVideoModel.objects.filter(day=pk)
    # audios = DayAudioModel.objects.filter(day=pk)
    # articles = DayArticleModel.objects.filter(day=pk)

    context = {
        'description': description,
        # 'photos': photos,
        # 'videos': videos,
        # 'audios': audios,
        # 'articles': articles,
    }

    return render(request, 'battle/current_event.html', context=context)


def articles(request, pk=None):
    articles = DayArticleModel.objects.all()
    return render(request, 'battle/current_event.html', {'articles': articles})


def about(request):
    return render(request, 'battle/about.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], 'piligriman@yahoo.com', ['eugene_chernyshev@yahoo.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Thank you for interesting to me')
                return redirect('battle:contacts')
            else:
                messages.error(request, 'Something went wrong')
    else:
        form = ContactForm()
    return render(request, 'battle/contact.html', {'form': form})



def day_list(request):
    day_list = GeneralDayDescriptionModel.objects.all()
    day_list_paginator = Paginator(day_list, 15)
    day_list_page_number = request.GET.get('page')
    day_list_object = day_list_paginator.get_page(day_list_page_number)
    return render(request, 'battle/day_list.html', {'day_list': day_list, 'day_list_object': day_list_object})