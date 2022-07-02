from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
    path('battle/', include(('battle.urls', 'battle'), namespace='battle')),
    path('crm_customers/', include(('crm_customers.urls', 'crm_customers'), namespace='crm_customers')),
    path('crm_employees/', include(('crm_employees.urls', 'crm_employees'), namespace='crm_employees')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'shop.views.handler404'
