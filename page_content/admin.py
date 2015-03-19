from django.contrib import admin
from page_content.models import *


class LogoAdmin(admin.ModelAdmin):
    list_display = ('label',)

    fieldsets = (
        (None, {
            'fields': ('site', 'label', 'image')
        }),

    )

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


class PageSectionInline(admin.TabularInline):
    model = PageSection
    sortable_field_name = "display_order"
    extra = 1


class WebPageAdmin(admin.ModelAdmin):
    model = WebPage
    list_display = ('label', 'is_published', 'create_date')
    list_filter = ('modified_date', 'is_published')
    list_editable = ('is_published',)

    prepopulated_fields = {'slug': ('label',), }
    search_fields = ('label',)
    save_as = True

    inlines = [
        PageSectionInline,
    ]

    fieldsets = (

        (None, {
            'classes': ('suit-tab suit-tab-general full-width',),
            'fields': ('template_choice', 'label', 'image_cover', 'is_published')
        }),

        (None, {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ('meta_title', 'meta_description', 'meta_tags', 'slug')
        }),

    )

    suit_form_includes = (
        ('admin/suit_includes/edit_page_content.html', 'bottom', 'general'),
    )

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO'))

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


class SocialLinkInline(admin.TabularInline):
    model = FooterSocialLink
    sortable_field_name = 'order'
    extra = 1


class FooterAdmin(admin.ModelAdmin):
    list_display = ('label',)

    fieldsets = (
        (None, {
            'fields': ('site', 'label')
        }),

    )

    inlines = [
        SocialLinkInline,
    ]

    suit_form_includes = (
        ('admin/suit_includes/edit_footer_content.html', 'bottom', 'general'),
    )

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


admin.site.register(Logo, LogoAdmin)
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(Footer, FooterAdmin)