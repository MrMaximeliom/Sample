from django.contrib import admin
from django.urls import path
from Address.admin import address_admin_site
urlpatterns = [
    path('admin/', admin.site.urls),
]
