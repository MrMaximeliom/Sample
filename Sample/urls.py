from django.contrib import admin
from django.urls import path
from Address.admin import address_admin_site
urlpatterns = [
    path('state-admin/', admin.site.urls),
    path('address-admin/', address_admin_site.urls),
]
