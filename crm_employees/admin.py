from django.contrib import admin

from .models import CustomerRecipientInfoModel, BoxOrderModel, \
    DeliveryParcelModel, BoxTariffModel, DeliveryTariffModel, \
    CourierTariffModel, CustomerDiscountModel


class CustomerRecipientInfoInline(admin.TabularInline):
    model = CustomerRecipientInfoModel


@admin.register(CustomerRecipientInfoModel)
class CustomerRecipientInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'address', 'email']
    list_display_links = ['name', 'surname']
    search_fields = ['email', 'name', 'surname', 'phone']
    edit_fields = ['phone', 'address', 'email']
    save_on_top = True
    list_per_page = 15


@admin.register(BoxOrderModel)
class BoxOrderAdmin(admin.ModelAdmin):
    list_display = ['ordering_date', 'size_ten', 'size_twenty', 'size_thirty', 'completed_at']


@admin.register(DeliveryParcelModel)
class DeliveryParcelAdmin(admin.ModelAdmin):
    list_display = ['email', 'sender_name', 'recipient', 
    'delivery_amount', 'courier','total_amount','weight', 'width', 'height', 'length']

    def email(self, obj):
        return obj.sender.email

    def sender_name(self, obj):
        return f'{obj.sender.name} {obj.sender.surname}'


@admin.register(DeliveryTariffModel)
class DeliveryTariffAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name', ]
    list_editable = ['price']


@admin.register(BoxTariffModel)
class BoxTariffAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name', ]
    list_editable = ['price']


@admin.register(CourierTariffModel)
class CourierTariffAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name', ]
    list_editable = ['price']


@admin.register(CustomerDiscountModel)
class CustomerDiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'value']
    list_display_links = ['code', ]
    list_editable = ['value']