from django.contrib.admin import AdminSite
from .models import Country,State,City
class AddressAdminSite(AdminSite):
    site_header = "Address Admin"
    site_title = "Address Admin Portal"
    index_title = "Welcome to Address Admin"
address_admin_site = AddressAdminSite(name='address_admin')
address_admin_site.register(Country)
address_admin_site.register(State)
address_admin_site.register(City)