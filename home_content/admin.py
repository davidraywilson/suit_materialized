from django.contrib import admin
from home_content.models import HomeSection, Billboard, MiniBillboard


class SectionAdmin(admin.ModelAdmin):
    model = HomeSection
    list_display = ('name', 'order', 'is_published')
    list_editable = ('order', 'is_published')

    fieldsets = (
        (None, {
            'fields': ('template', 'name', 'order', 'is_published')
        }),
        (None, {
            'fields': ('image_background',)
        }),

    )

    class Media:
        js = [
            '/static/admin_js/home_section.js',
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


class BillboardAdmin(admin.ModelAdmin):
    model = Billboard
    list_display = ('name', 'order', 'publish_date', 'is_published')
    list_filter = ('publish_date', 'is_published')
    list_editable = ('order', 'is_published',)

    fieldsets = (

        (None, {
            'classes': (),
            'fields': ('name', 'order', 'image', 'header', 'sub_header', 'publish_date', 'expire_date', 'is_published')
        }),

    )

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


class MiniBillboardAdmin(admin.ModelAdmin):
    model = MiniBillboard
    list_display = ('name', 'order', 'publish_date', 'is_published')
    list_filter = ('publish_date', 'is_published')
    list_editable = ('order', 'is_published',)

    fieldsets = (

        (None, {
            'classes': (),
            'fields': ('name', 'order', 'publish_date', 'expire_date', 'is_published')
        }),

        (None, {
            'classes': (),
            'fields': ('size', 'image', 'video', 'link')
        }),

    )

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


admin.site.register(HomeSection, SectionAdmin)
admin.site.register(Billboard, BillboardAdmin)
admin.site.register(MiniBillboard, MiniBillboardAdmin)