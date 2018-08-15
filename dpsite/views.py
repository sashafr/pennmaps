from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from django.template import Context, loader
from django.conf import settings

# Request Functions
def base(request):
    return render(request, 'dpsite/base.html')

def home(request):
    return render(request, 'dpsite/index.html')

def mapItem(request):
    mapItem = MapItem.objects.all()

    context = {'map_items': mapItem}
    return render(request, 'dpsite/Test.html',context)

def webSeries(request):
    seasons = WebSeries.objects.values('season').distinct()
    series = {}
    for season_number in seasons:
        series[season_number['season']] = WebSeries.objects.filter(season=season_number['season'])
    page_styles = '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/mediagallery.css" type="text/css">'
    sidebar_text = ""
    getsidebar = PageText.objects.filter(text_hook="webseries_sidebar")
    if getsidebar:
        sidebar_text = getsidebar[0].page_text
    context = {'series': series, 'page_styles': page_styles, "sidebar_text": sidebar_text}
    return render(request, 'dpsite/webseries.html', context)

def mediaGallery(request, tag=""):
    if tag != "":
        media = Media.objects.filter(tags__slug = tag)
    else:
        media = Media.objects.all()
    page_styles = '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/mediagallery.css" type="text/css">'
    sidebar_text = ""
    getsidebar = PageText.objects.filter(text_hook="media_sidebar")
    if getsidebar:
        sidebar_text = getsidebar[0].page_text
    tagobject = Tag.objects.filter(slug = tag)
    if tagobject:
        pagetag = tagobject[0]
    else:
        pagetag = ""
    context = {'media': media, 'page_styles': page_styles, 'tag': pagetag, 'sidebar_text': sidebar_text }
    return render(request, 'dpsite/mediaGallery.html', context)

def archiveSearch(request):
    items = MapItem.objects.all()
    context = {'items': items, }
    return render(request, 'dpsite/search.html', context)

def archiveGallery(request, tag=""):
    if tag != "":
        items = MapItem.objects.filter(tags__slug = tag)
    else:
        items = MapItem.objects.all()
    context = {'items': items, 'tag': tag }
    return render(request, 'dpsite/archiveGallery.html', context)

def archiveItem(request, id):
    mapItem = get_object_or_404(MapItem, pk = id)
    page_styles = '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/mediagallery.css" type="text/css">'
    context = {'mapItem': mapItem, 'page_styles': page_styles }
    return render(request, 'dpsite/mapItem.html', context)

def aboutTeam(request):
    return render(request, 'dpsite/aboutTeam.html')

def aboutProject(request):
    return render(request, 'dpsite/aboutProject.html')

def map(request):
    mapItem = MapItem.objects.all()
    partOfCity = PartOfCity.objects.all()
    context = {'map_items': mapItem, 'part_of_city': partOfCity}
    return render(request, 'dpsite/Test.html',context)
