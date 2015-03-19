from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'webapp.views',
    url(r'^$', 'view_home'),
)

urlpatterns += patterns(
    '',
    url(r'^front-edit/', include('front.urls')),
)

urlpatterns += patterns(
    '',
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEVELOPMENT:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns(
    'categories.views',
    url(r'^edit/category-item/(?P<a_id>.*)$', 'edit_category_item'),
    url(r'^category/(?P<a_slug>.*)/(?P<b_slug>.*)$', 'view_category_item'),
    url(r'^category/(?P<a_slug>.*)$', 'view_category'),
)

urlpatterns += patterns(
    'page_content.views',
    url(r'^edit/(?P<a_slug>.*)$', 'edit_web_page'),
    url(r'^(?P<a_slug>.*)$', 'view_web_page'),
)