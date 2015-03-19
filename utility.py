import logging
from django.contrib.sites.models import Site
from navigation.models import PrimaryNavigation
from page_content.models import Logo, Footer


def set_detail_context(request, a_context):
    # CHECK FOR ADMIN USER
    active_user = None
    try:
        if request.user.is_superuser:
            active_user = request.user

    except Exception, e:
        print e

    a_context['active_user'] = active_user

    # NAV LINKS
    desktop_links = PrimaryNavigation.get_published_objects()
    a_context['desktop_links'] = desktop_links

    nav_links = PrimaryNavigation.get_published_objects()
    a_context['nav_links'] = nav_links

    try:
        # GET CURRENT SITE
        current_site = Site.objects.get_current()

    except Exception, e:
        logging.error(e)
        current_site = None

    if current_site:
        try:
            # GET LOGO FOR CURRENT SITE
            logo = Logo.objects.get(site=current_site)

        except Exception, e:
            logging.error(e)
            logo = None

        try:
            # GET FOOTER FOR CURRENT SITE
            footer = Footer.objects.get(site=current_site)

        except Exception, e:
            logging.error(e)
            footer = None

    else:
        logo = None
        footer = None

    a_context['logo'] = logo
    a_context['footer'] = footer