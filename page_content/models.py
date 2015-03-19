from django.contrib.sites.models import Site
from django.db import models
from filebrowser.fields import FileBrowseField


class Logo(models.Model):
    site = models.OneToOneField(Site)
    label = models.CharField(max_length=100, help_text='This is only used in the admin.')
    image = FileBrowseField(max_length=400, blank=True, null=True, help_text='Transparent .png')

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'


TEMPLATE_CHOICES = (
    ('contact', 'Contact'),
)


class WebPage(models.Model):
    template_choice = models.CharField(max_length=50, blank=True, null=True, choices=TEMPLATE_CHOICES)

    label = models.CharField(max_length=100)
    slug = models.SlugField()

    meta_title = models.CharField(max_length=100, blank=True, null=True, help_text='This shows at the top of the browser, usually in the tab.')
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_tags = models.CharField(max_length=500, blank=True, null=True)

    image_cover = FileBrowseField(max_length=400, blank=True, null=True, help_text='Roughly 1400px by 400px',
                                  verbose_name='Cover image')

    is_published = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.label

    def url(self):
        return '/%s' % self.slug

    def get_absolute_url(self):
        return self.url()

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ('label',)

    @staticmethod
    def get_published_objects():
        return WebPage.objects.filter(is_published=True)

    def sections(self):
        return self.pagesection_set.filter(is_published=True)


SECTION_TEMPLATES = (
    ('1_col', '1 Column'),
    ('2_col', '2 Column'),
    ('2_col_left', '2 Column Wide Left'),
    ('2_col_right', '2 Column Wide Right'),
)


class PageSection(models.Model):
    page = models.ForeignKey(WebPage)
    label = models.CharField(max_length=400)

    template = models.CharField(max_length=50, blank=True, null=True, choices=SECTION_TEMPLATES)

    image = FileBrowseField(max_length=400, blank=True, null=True, verbose_name='Section image',
                            help_text='At least 1140px wide')

    display_order = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ('display_order', 'label')

    @staticmethod
    def get_published_objects():
        objects = PageSection.objects.filter(is_published=True).order_by('display_order', 'label')

        return objects


class Footer(models.Model):
    site = models.OneToOneField(Site)
    label = models.CharField(max_length=100, help_text='This is only used in the admin.')

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

    def social_links(self):
        return self.footersociallink_set.order_by('order')


class FooterSocialLink(models.Model):
    parent = models.ForeignKey(Footer)
    label = models.CharField(max_length=200)

    image = FileBrowseField(max_length=400)
    link = models.URLField()

    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'
        ordering = ('order', 'label')