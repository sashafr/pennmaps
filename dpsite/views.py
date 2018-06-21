from django.shortcuts import render
from django.http import HttpResponse
from .models import MapItem

# Create your views here.
def index(request):
	return HttpResponse("Diggin' Philly data index.")

def mapItem(request):
	mapItem = MapItem.objects.all()
	context = {'map_items': mapItem}
	return render(request, 'dpsite/Test.html',context)
