from django.contrib import admin
from shop.models import MenuTagModel, DiscountModel, ProductCategoryModel, ProductModel, ProductAdditionalPhoto, OrderModel, OrderLineModel



# Register your models here.
class ProductAdditionalInline(admin.TabularInline):
    model = ProductAdditionalPhoto


@admin.register(MenuTagModel)
class MenuTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
    list_display_links = ['name']


@admin.register(DiscountModel)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'value']
    list_display_links = ['value']
    list_editable = ['code']


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    list_display_links = ['category']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'price', 'in_stock', 'description']
    list_display_links = ['name']
    inlines = [ProductAdditionalInline]


    def image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}">')
        else:
            '-'

    image.short_description = 'Photo'


@admin.register(OrderModel)
class BoxOrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id', ]


@admin.register(OrderLineModel)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id', ]
