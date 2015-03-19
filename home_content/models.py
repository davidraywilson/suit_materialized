import datetime
from django.db import models
from django.db.models import Q
from filebrowser.fields import FileBrowseField


TEMPLATES = (
    ('billboard', 'Billboards'),
    ('mini_billboard', 'Mini Billboards'),
    ('1_col', '1 Column Free Form'),
    ('2_col', '2 Column Free Form'),
    ('map', 'Map'),
)


class HomeSection(models.Model):
    name = models.CharField(max_length=200)

    template = models.CharField(max_length=50, choices=TEMPLATES, default='s')
    image_background = FileBrowseField(max_length=200, blank=True, null=True, help_text='Leave blank for white.', verbose_name='Background image')

    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=1, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ('order',)

    @staticmethod
    def get_published_objects():
        sections = HomeSection.objects.filter(is_published=True).order_by('order')
        return sections


class Billboard(models.Model):
    name = models.CharField(max_length=200)

    image = FileBrowseField(max_length=200, help_text='Approximately 1000 px wide by 650 px tall. (Keep subject towards the middle of image for best viewing on mobile.)')
    header = models.CharField(max_length=35, blank=True, null=True)
    sub_header = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    publish_date = models.DateField(db_index=True)
    expire_date = models.DateField(null=True, blank=True)

    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Billboard'
        verbose_name_plural = 'Billboards'
        ordering = ('order', '-publish_date')

    @staticmethod
    def get_published_objects():
        billboards = Billboard.objects.filter(Q(publish_date__lte=datetime.datetime.now) & Q(is_published=True) &
                                              (Q(expire_date=None) | Q(expire_date__gte=datetime.datetime.now))).order_by('order', '-publish_date')
        return billboards


SIZES = (
    ('s', 'Small'),
    ('l', 'Large')
)


class MiniBillboard(models.Model):
    name = models.CharField(max_length=200)

    image = FileBrowseField(max_length=200, blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True, help_text='Embed video from Vimeo (preferably) or YouTube.')
    size = models.CharField(max_length=50, choices=SIZES, default='s')
    link = models.CharField(max_length=200, blank=True, null=True)

    is_published = models.BooleanField(default=True)
    publish_date = models.DateField(db_index=True)
    expire_date = models.DateField(null=True, blank=True)

    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Mini Billboard'
        verbose_name_plural = 'Mini Billboards'
        ordering = ('order', '-publish_date')

    @staticmethod
    def get_published_objects():
        mini_billboards = MiniBillboard.objects.filter(Q(publish_date__lte=datetime.datetime.now) & Q(is_published=True) &
                                                       (Q(expire_date=None) | Q(expire_date__gte=datetime.datetime.now))).order_by('order', '-publish_date')
        return mini_billboards