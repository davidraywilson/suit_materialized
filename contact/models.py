from django.contrib.sites.models import Site
from django.db import models


class ContactLead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    date = models.DateField()

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Contact Leads'
        verbose_name = 'Contact Lead'
        ordering = ('-date', 'first_name', 'last_name')


class ContactMap(models.Model):
    site = models.OneToOneField(Site)
    label = models.CharField(max_length=100, help_text='This is only used in the admin.')
    iframe = models.CharField(max_length=400, help_text='You can get this from Google Maps.')

    def __unicode__(self):
        return self.label