import logging
from django.shortcuts import render_to_response
from django.template import RequestContext
from home_content.models import HomeSection, Billboard, MiniBillboard
from utility import set_detail_context


def view_home(request):
    try:
        sections = HomeSection.get_published_objects()
        billboards = Billboard.get_published_objects()
        mini_billboards = MiniBillboard.get_published_objects()

    except Exception, e:
        logging.error(e)
        sections = None
        billboards = None
        mini_billboards = None

    context = {'sections': sections, 'billboards': billboards, 'mini_billboards': mini_billboards}
    set_detail_context(request, context)

    template = 'home.html'

    return render_to_response(template, context, context_instance=RequestContext(request))