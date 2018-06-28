from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import MapItem, WebSeries, Media
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
    context = {'series': series, 'dummmyvariable': 'Helloworld'}
    return render(request, 'dpsite/webseries.html', context)

def mediaItem(request):
    mediaitem = Media.objects.all()
    context = {'mediaitem': mediaitem}
    return render(request, 'dpsite/mediaItem.html', context)
