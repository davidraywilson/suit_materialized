import logging
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from categories.models import Category, CategoryItem
from utility import set_detail_context


def view_category(request, a_slug):
    try:
        category = Category.objects.get(slug=a_slug, is_published=True)

    except Exception, e:
        logging.error(e)
        raise Http404

    context = {'category': category}
    set_detail_context(request, context)

    template = 'categories/category.html'

    return render_to_response(template, context, context_instance=RequestContext(request))


def edit_category_item(request, a_id):
    try:
        category = None
        category_item = CategoryItem.objects.get(id=a_id)

        related_items = None

    except Exception, e:
        logging.error(e)
        raise Http404

    context = {'category': category, 'category_item': category_item, 'related_items': related_items}
    set_detail_context(request, context)

    template = 'categories/category_detail.html'

    return render_to_response(template, context, context_instance=RequestContext(request))


def view_category_item(request, a_slug, b_slug):
    try:
        category = Category.objects.get(slug=a_slug, is_published=True)
        category_item = CategoryItem.objects.get(slug=b_slug, is_published=True)

        related_items = CategoryItem.get_related_items(category_item, category)

    except Exception, e:
        logging.error(e)
        raise Http404

    context = {'category': category, 'category_item': category_item, 'related_items': related_items}
    set_detail_context(request, context)

    template = 'categories/category_detail.html'

    return render_to_response(template, context, context_instance=RequestContext(request))