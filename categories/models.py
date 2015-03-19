import logging
from django.db import models
from filebrowser.fields import FileBrowseField


class Category(models.Model):
    label = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    meta_title = models.CharField(max_length=100, blank=True, null=True, help_text='This shows at the top of the browser, usually in the tab.')
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_tags = models.CharField(max_length=500, blank=True, null=True)

    image_cover = FileBrowseField(max_length=400, blank=True, null=True, verbose_name='Cover image')

    order = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)

    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.label

    def url(self):
        return '/category/%s' % self.slug

    def get_absolute_url(self):
        return self.url()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('order', 'label')

    @staticmethod
    def get_published_objects():
        return Category.objects.filter(is_published=True)

    def children(self):
        return self.categoryitem_set.filter(is_published=True)


class CategoryItem(models.Model):
    label = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    meta_title = models.CharField(max_length=100, blank=True, null=True, help_text='This shows at the top of the browser, usually in the tab.')
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_tags = models.CharField(max_length=500, blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True, null=True)

    image_cover = FileBrowseField(max_length=400, blank=True, null=True, verbose_name='Cover image')
    image_teaser = FileBrowseField(max_length=400, blank=True, null=True, help_text='360px by 240px', verbose_name='Teaser image')

    external_link = models.URLField(blank=True, null=True)

    order = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)

    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Category Item'
        verbose_name_plural = 'Category Items'
        ordering = ('order', 'label')

    def images(self):
        return self.slideshowimage_set.order_by('order')

    def social_links(self):
        return self.sociallink_set.order_by('order')

    @staticmethod
    def get_related_items(category_item, category):
        try:
            items = CategoryItem.objects.filter(is_published=True, categories=category).exclude(id=category_item.id).order_by('order', 'label')[0:4]
        except Exception, e:
            logging.error(e)
            items = None

        return items


class SlideShowImage(models.Model):
    parent = models.ForeignKey(CategoryItem)
    label = models.CharField(max_length=200)

    image = FileBrowseField(max_length=400, help_text='608px by 516px')

    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Slide Show Image'
        verbose_name_plural = 'Slide Show Images'
        ordering = ('order', 'label')


class SocialLink(models.Model):
    parent = models.ForeignKey(CategoryItem)
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