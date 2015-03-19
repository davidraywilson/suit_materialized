from django.contrib import admin
from models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date')

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


class MapAdmin(admin.ModelAdmin):
    list_display = ('label',)


admin.site.register(ContactLead, ContactAdmin)
admin.site.register(ContactMap, MapAdmin)