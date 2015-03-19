from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from contact.views import view_contact

from page_content.models import WebPage
from utility import set_detail_context


def edit_web_page(request, a_slug):
    edit = True
    return view_web_page(request, a_slug, edit)


# Some templates need extra or special processing to retrieve additional data. This map
# defines which templates get a special controller.
TEMPLATE_CONTROLLER_MAP = {'contact': view_contact}


def view_web_page(request, a_slug, edit=None):
    try:
        # IF WE ARE IN EDIT MODE, WE NEED TO LOOK FOR ALL PAGES
        # REGARDLESS OF IT'S PUBLISHED STATE
        if edit:
            page = WebPage.objects.get(id=a_slug)

        else:
            page = WebPage.objects.get(slug=a_slug, is_published=True)

    except:
        raise Http404

    # CHECK FOR TEMPLATE OVERRIDE
    try:
        if page.template_choice != None and len(page.template_choice) > 1:

            # IF TEMPLATE OVERRIDE, REDIRECT TO CORRECT VIEW
            if TEMPLATE_CONTROLLER_MAP.has_key(page.template_choice):
                func_ptr = TEMPLATE_CONTROLLER_MAP[page.template_choice]
                return func_ptr(request, page)

    except Exception:
        pass

    context = {'page': page}
    set_detail_context(request, context)

    template = 'detail_page.html'

    return render_to_response(template, context, context_instance=RequestContext(request))