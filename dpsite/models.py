#from django.db import models
from django.contrib.gis.db import models

from datetime import date

# Create your models here.

class TagGroup(models.Model):
	title = models.CharField(max_length = 50)

class Tag(models.Model):
	title = models.CharField(max_length = 50)
	tag_group = models.ForeignKey('TagGroup',on_delete=models.CASCADE,)

class OverlayGroup(models.Model):
	title = models.CharField(max_length = 50)

class Media(models.Model):
	title = models.CharField(max_length = 50)
	description = models.CharField(max_length = 200)
	credits = models.CharField(max_length=50)
	date_created = models.DateField('date', default=date.today)
	file_upload = models.FileField()
	file_url = models.URLField(max_length=200)
	tags = models.ManyToManyField('Tag')
	start_date = models.DateField('start date',default=date.today)
	end_date = models.DateField('end date',default=date.today)
	media_sources = models.CharField(max_length = 200)

class MapItem(models.Model):
	title = models.CharField(max_length = 50)
	#summary = models.CharField(max_length = 300)
	#description = models.CharField(max_length = 1000)
	info_sources = models.CharField(max_length = 1000)
	location_notes = models.CharField(max_length = 50)
	start_date = models.DateField('start date',default=date.today)
	end_date = models.DateField('end date',default=date.today)
	status = models.CharField(max_length = 50)
	location1 = models.MultiPointField()
	location2 = models.MultiPolygonField()
	tags = models.ManyToManyField('Tag')
	media = models.ManyToManyField('Media')
	min_zoom = models.IntegerField()
	max_zoom = models.IntegerField()
	overlay_group = models.ManyToManyField('OverlayGroup')

class WebSeries(models.Model):
	title = models.CharField(max_length = 50)
	description = models.CharField(max_length = 200)
	date = models.DateField('date', default=date.today)
	season = models.IntegerField()
	episode = models.IntegerField()
	file_upload = models.FileField()
	file_url = models.URLField(max_length=200)
	map_location = models.ForeignKey('MapItem',on_delete=models.CASCADE,)
	tags = models.ManyToManyField('Tag')
	part_of_city = models.CharField(max_length=50)
	time_period = models.CharField(max_length=50)
	credits = models.CharField(max_length=50)

class PartOfCity(models.Model):
	title = models.CharField(max_length = 50)
	start_date = models.DateField('start date',default=date.today)
	end_date = models.DateField('end date',default=date.today)

class TimePeriod(models.Model):
	title = models.CharField(max_length = 50)
	start_date = models.DateField('start date',default=date.today)
	end_date = models.DateField('end date',default=date.today)
