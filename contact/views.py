import datetime
import logging
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from contact.forms import ContactForm
from contact.models import ContactLead, ContactMap
from utility import set_detail_context


def view_contact(request, page):
    message = False

    try:
        # GET MAP FOR CURRENT SITE
        current_site = Site.objects.get_current()
        contact_map = ContactMap.objects.get(site=current_site)

    except Exception, e:
        logging.error(e)
        contact_map = None

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            cleaned_data = contact_form.cleaned_data

            lead = ContactLead()
            lead.first_name = cleaned_data['first_name']
            lead.last_name = cleaned_data['last_name']
            lead.email = cleaned_data['email']
            lead.message = cleaned_data['message']
            lead.date = datetime.datetime.now()
            lead.save()

            # SEND EMAIL
            email_context = {'contactLead': lead}

            subject, from_email, to_email = 'New Contact Lead', settings.DEFAULT_FROM_EMAIL, [settings.ONLINE_CONTACT_EMAIL]
            text_content = render_to_string("email/contact/new_contact_lead_string.html", email_context)
            html_content = render_to_string("email/contact/new_contact_lead_html.html", email_context)
            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            message = True

    else:
        contact_form = ContactForm()

    context = {'page': page, 'map': contact_map, 'contact_form': contact_form, 'message': message}
    set_detail_context(request, context)

    template = 'overrides/contact.html'

    return render_to_response(template, context, context_instance=RequestContext(request))