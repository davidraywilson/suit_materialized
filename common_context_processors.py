import logging
from django.conf import settings
from django.contrib.sites.models import Site


def common_context(request):
    try:
        # GET CURRENT SITE
        current_site = Site.objects.get_current()

    except Exception, e:
        logging.error(e)
        current_site = None

    try:
        django_front_key = settings.DJANGO_FRONT_KEY

    except Exception, e:
        logging.error(e)
        django_front_key = current_site

    return {'django_front_key': django_front_key}