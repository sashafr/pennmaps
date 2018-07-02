from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from django.template import Context, loader


# Request Functions
def base(request):
    return render(request, 'dpsite/base.html')
    #template = loader.get_template("dpsite/index.html")
    #return HttpResponse(template.render())
	#return HttpResponse("Diggin' Philly data index.")

def mapItem(request):
	mapItem = MapItem.objects.all()
	context = {'map_items': mapItem}
	return render(request, 'dpsite/Test.html',context)

def webSeries(request):
    series = WebSeries.objects.all()
    context = {'series': series,}
    return render(request, 'dpsite/webseries.html', context)

def mediaItem(request):
    mediaitem = Media.objects.all()
    context = {'mediaitem': mediaitem}
    return render(request, 'dpsite/mediaItem.html', context)

def mediaGallery(request, tag=""):
    if tag != "":
        media = Media.objects.filter(tags__slug = tag)
    else:
        media = Media.objects.all()
    context = {'media': media, 'tag': tag }
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
    context = {'mapItem': mapItem, }
    return render(request, 'dpsite/mapItem.html', context)

def aboutTeam(request):
    return render(request, 'dpsite/aboutTeam.html')

def aboutProject(request):
    return render(request, 'dpsite/aboutProject.html')

def map(request):
	mapItem = MapItem.objects.all()
	context = {'map_items': mapItem}
	return render(request, 'dpsite/Test.html',context)
