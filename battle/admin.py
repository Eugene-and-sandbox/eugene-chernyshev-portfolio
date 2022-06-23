from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import GeneralDayDescriptionModel, DayEventModel, \
    DayPhotoModel, DayVideoModel, DayAudioModel, \
    DayArticleModel, LostItemsListModel, ItemCategoryModel


# Register your models here.
@admin.register(GeneralDayDescriptionModel)
class GeneralDayDescriptionAdmin(admin.ModelAdmin):
    list_display = ['day_number', 'date', 'day_title', 'daily_image']
    list_display_links = ['day_number', 'date']
    list_editable = ['day_title']
    list_per_page = 10
    search_fields = ['day_number', 'date', 'day_title']
    save_on_top = True

    def daily_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}"> width="50"')
        return '-'

    daily_image.short_description = 'Photo'


@admin.register(DayEventModel)
class DayEventAdmin(admin.ModelAdmin):
    list_display = ['day', 'event_time']


@admin.register(DayPhotoModel)
class DayPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'parent_event_time',
                    'description', 'media', 'category']
    list_display_links = ['id', 'parent']
    search_fields = ['parent']
    ordering = ['parent']
    list_per_page = 25


@admin.register(DayVideoModel)
class DayVideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'parent_event_time',
                    'category', 'description', 'media']
    list_display_links = ['id', 'parent']
    search_fields = ['parent']
    ordering = ['parent']
    list_per_page = 25


@admin.register(DayAudioModel)
class DayAudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'parent_event_time',
                    'category', 'description', 'media']
    list_display_links = ['id', 'parent']
    search_fields = ['parent']
    ordering = ['parent']
    list_per_page = 25


@admin.register(DayArticleModel)
class DayArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'parent_event_time',
                    'category', 'description']
    list_display_links = ['id', 'parent']
    search_fields = ['parent']
    ordering = ['parent']
    list_per_page = 25


@admin.register(LostItemsListModel)
class LostItemsListAdmin(admin.ModelAdmin):
    list_display = ['team', 'tanks', 'battle_armored_vehicle',
                    'artilery_system', 'rszo', 'antyair_missle',
                    'airplanes', 'helicopters', 'vehicles',
                    'ships_and_boats', 'bpla', 'special_vehicle',
                    'rockets']
    list_display_links = ['team', 'tanks']


@admin.register(ItemCategoryModel)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    list_display_links = ['category']
