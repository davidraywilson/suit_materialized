from django.db import models
from categories.models import Category, CategoryItem
from page_content.models import WebPage


LINK_TYPES = (
    ('page', 'Page'),
    ('category', 'Category '),
    ('custom', 'Link')
)


class PrimaryNavigation(models.Model):
    title = models.CharField(max_length=100)

    link_type = models.CharField(max_length=50, blank=True, null=True, choices=LINK_TYPES)

    page = models.ForeignKey(WebPage, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def url(self):
        if self.page:
            return '%s' % self.page.get_absolute_url()

        elif self.category:
            return '%s' % self.category.get_absolute_url()

        elif self.link:
            return '%s' % self.link

        else:
            return '#'

    def get_absolute_url(self):
        return self.url()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Primary Navigation'
        verbose_name_plural = 'Primary Navigation'
        ordering = ('order', 'title')

    @staticmethod
    def get_published_objects():
        return PrimaryNavigation.objects.filter(is_published=True)

    def links(self):
        return self.subprimarynavigation_set.filter(is_published=True)


class SubPrimaryNavigation(models.Model):
    parent = models.ForeignKey(PrimaryNavigation, verbose_name='Parent link')
    title = models.CharField(max_length=100)

    link_type = models.CharField(max_length=50, blank=True, null=True, choices=LINK_TYPES)

    page = models.ForeignKey(WebPage, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def url(self):
        if self.page:
            return '%s' % self.page.get_absolute_url()

        elif self.category:
            return '%s' % self.category.get_absolute_url()

        elif self.link:
            return '%s' % self.link

        else:
            return '#'

    def get_absolute_url(self):
        return self.url()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Sub Primary Navigation'
        verbose_name_plural = 'Sub Primary Navigation'
        ordering = ('order', 'title')

    @staticmethod
    def get_published_objects():
        return SubPrimaryNavigation.objects.filter(is_published=True)