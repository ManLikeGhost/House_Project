from django.contrib import admin

from .models import Contacts


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_feilds = ('name', 'email', 'listing')
    list_per_page = 10

admin.site.register(Contacts, ContactAdmin)
