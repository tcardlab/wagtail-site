from __future__ import absolute_import, unicode_literals

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })


from django.http import JsonResponse, HttpResponse
import json


# def getQuora(request):
#     data = open('search/a.json')
#     data1 = json.load(data)  # deserialises it
#     data2 = json.dumps(data1)  # json formatted string
#     data.close()
#     return HttpResponse(data2, content_type='application/json')

# required for get requests that dont rely on static
def getQuora(request):
    data = open('search/a.json')
    data1 = json.load(data)  # deserialises it
    data.close()
    return JsonResponse(data1)
