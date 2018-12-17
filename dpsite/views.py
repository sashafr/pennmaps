from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from django.template import Context, loader
from django.conf import settings
from .forms import SearchForm

# Request Functions
def base(request):
    return render(request, 'dpsite/base.html')

def home(request):
    site = Site.objects.get_current()
    if site:
        configs = SiteConfig.objects.filter(site = site)
    if configs:
        config = configs[0]
    else:
        config = ""
    slides = HomeSlide.objects.all().order_by('order')
    fb = settings.FACEBOOK_URL
    insta = settings.INSTAGRAM_URL
    tw = settings.TWITTER_URL
    context = {'slides': slides, 'configs': config, 'fb_url': fb, 'insta_url': insta, 'tw_url': tw}
    return render(request, 'dpsite/index.html', context)

def aboutProject(request):
    site = Site.objects.get_current()
    if site:
        configs = SiteConfig.objects.filter(site = site)
    if configs:
        config = configs[0]
    else:
        config = ""
    context = {'configs': config}
    return render(request, 'dpsite/aboutProject.html', context)

def aboutTeam(request):
    site = Site.objects.get_current()
    if site:
        configs = SiteConfig.objects.filter(site = site)
    if configs:
        config = configs[0]
    else:
        config = ""
    context = {'configs': config}
    return render(request, 'dpsite/aboutTeam.html', context)

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
    return render(request, 'dpsite/webseriestemp.html', context)

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

def archiveGallery(request, tag=""):
    if tag != "":
        items = MapItem.objects.filter(tags__slug = tag)
        active_tag = Tag.objects.filter(slug = tag)
        if active_tag:
            active_tag = active_tag[0]
        else:
            active_tag = ""
    else:
        items = MapItem.objects.all()
        active_tag = ""
    page_styles = '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/mediagallery.css" type="text/css">'
    context = {'items': items, 'tag': active_tag, 'page_styles': page_styles }
    return render(request, 'dpsite/archiveGallery.html', context)

def archiveItem(request, id):
    mapItem = get_object_or_404(MapItem, pk = id)
    page_styles = '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/mediagallery.css" type="text/css">'
    context = {'mapItem': mapItem, 'page_styles': page_styles }
    return render(request, 'dpsite/mapItem.html', context)

def map(request):
    site = Site.objects.get_current()
    if site:
        configs = SiteConfig.objects.filter(site = site)
    if configs:
        config = configs[0]
    else:
        config = ""
    page_styles = '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/map.css" type="text/css">'
    mapItem = MapItem.objects.all()
    partOfCity = PartOfCity.objects.all()
    tags = Tag.objects.filter(tag_group__title = "Themes")
    map_url = settings.MAP_XYZ_URL
    center = settings.MAP_CENTER_COORDS
    zoom = settings.MAP_ZOOM
    min_zoom = settings.MAP_MIN_ZOOM
    max_zoom = settings.MAP_MAX_ZOOM
    context = {'map_items': mapItem, 'part_of_city': partOfCity, 'configs': config, 'page_styles': page_styles, 'tags': tags, 'map_url': map_url, 'zoom': zoom, 'center': center, 'min_zoom': min_zoom, 'max_zoom': max_zoom }
    return render(request, 'dpsite/map.html',context)

def archiveSearch(request):
    item_name = request.GET.get('q', None)
    form = SearchForm(request.POST)
    form.is_valid()
    item_tags = form.cleaned_data.get('tagfield')
    context = {'form': form}
    if item_name:
        items = MapItem.objects.filter(description__icontains=item_name)
        context['items'] = items
        items_new = MapItem.objects.none()
        if item_tags:
            for tag in item_tags:
                items_new |= (items.filter(tags__title__icontains=tag))
            context['items'] = items_new.distinct
        else:
            context['items'] = items.distinct
        return render(request,"dpsite/search.html", context)
    else:
        items = MapItem.objects.all()
        items_new = MapItem.objects.none()
        if item_tags:
            for tag in item_tags:
                items_new |= (items.filter(tags__title__icontains=tag))
            context['items'] = items_new.distinct
        else:
            context['items'] = items.distinct
        return render(request,"dpsite/search.html", context)
