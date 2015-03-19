from django.contrib import admin
from models import *


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('label', 'order', 'is_published', 'create_date')
    list_filter = ('modified_date', 'is_published')
    list_editable = ('order', 'is_published')

    prepopulated_fields = {'slug': ('label',), }
    search_fields = ('label',)
    save_as = True

    fieldsets = (

        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('label', 'image_cover', 'order', 'is_published')
        }),

        (None, {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ('meta_title', 'meta_description', 'meta_tags', 'slug')
        }),

    )

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO'))

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


class ImageInline(admin.TabularInline):
    model = SlideShowImage
    sortable_field_name = 'order'
    extra = 1


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    sortable_field_name = 'order'
    extra = 1


class CategoryItemAdmin(admin.ModelAdmin):
    model = CategoryItem
    list_display = ('label', 'order', 'is_published', 'create_date')
    list_filter = ('modified_date', 'is_published')
    list_editable = ('order', 'is_published')

    prepopulated_fields = {'slug': ('label',), }
    search_fields = ('label',)
    save_as = True

    inlines = [
        ImageInline,
        SocialLinkInline,
    ]

    fieldsets = (

        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('label', 'categories', 'image_cover', 'image_teaser', 'teaser', 'external_link', 'order', 'is_published')
        }),

        (None, {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ('meta_title', 'meta_description', 'meta_tags', 'slug')
        }),

    )

    suit_form_includes = (
        ('admin/suit_includes/edit_category_item_description.html', 'bottom', 'general'),
    )

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO'))

    class Media:
        js = [
            '/static/admin_js/tinymce/tinymce.min.js',
            '/static/admin_js/tinymce_init.js'
        ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem, CategoryItemAdmin)
