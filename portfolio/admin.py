from django.contrib import admin
from portfolio.models import ExamplePreviewModel, ExampleCategoryModel
from django.utils.safestring import mark_safe 


# Register your models here.
@admin.register(ExamplePreviewModel)
class ExamplePreviewAdmin(admin.ModelAdmin):
    list_display = ['description', 'picture']
    list_display_links = ['description']

    def picture(self, obj):
        if obj.photo :
            mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    picture.short_description = 'Picture'


@admin.register(ExampleCategoryModel)
class ExampleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']