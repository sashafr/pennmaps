#from django.db import models
from django.contrib.gis.db import models

from datetime import date

# Create your models here.

class TagGroup(models.Model):
    title = models.CharField(max_length = 50)
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length = 50)
    tag_group = models.ForeignKey(
    'TagGroup',
    on_delete=models.CASCADE,)
    def __str__(self):
        return self.title

class Layer(models.Model):
    xyz = models.URLField(max_length=200)

class OverlayGroup(models.Model):
    title = models.CharField(max_length = 50)
    layer = models.ManyToManyField('Layer', through='OverlayGroupLayer')

class OverlayGroupLayer(models.Model):
    overlay_group = models.ForeignKey(OverlayGroup, on_delete=models.CASCADE)
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    order = models.IntegerField()

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
    def __str__(self):
        return self.title

class MapItem(models.Model):
    title = models.CharField(max_length = 50)
    summary = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    info_sources = models.CharField(max_length = 1000)
    location_notes = models.CharField(max_length = 50)
    start_date = models.DateField('start date',default=date.today)
    end_date = models.DateField('end date',default=date.today)
    status = models.CharField(max_length = 50)
    location1 = models.MultiPointField()
    location2 = models.MultiPolygonField()
    tags = models.ManyToManyField('Tag')
    media = models.ManyToManyField('Media', through = 'MappedMedia')
    min_zoom = models.IntegerField()
    max_zoom = models.IntegerField()
    overlay_group = models.ManyToManyField('OverlayGroup')
    def __str__(self):
        return self.title

class MappedMedia(models.Model):
    map_item = models.ForeignKey(MapItem, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    order = models.IntegerField()

class WebSeries(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    upload_date = models.DateField('date', default=date.today)
    season = models.IntegerField()
    episode = models.IntegerField()
    file_upload = models.FileField()
    file_url = models.URLField(max_length=200)
    map_location = models.ForeignKey('MapItem',on_delete=models.CASCADE,)
    tags = models.ManyToManyField('Tag')
    credits = models.CharField(max_length=50)
    start_date = models.DateField('start date',default=date.today)
    end_date = models.DateField('end date',default=date.today)

class PartOfCity(models.Model):
    title = models.CharField(max_length = 50)
    area = models.MultiPolygonField(default=None, blank=True, null=True)

class TimePeriod(models.Model):
    title = models.CharField(max_length = 50)
    start_date = models.DateField('start date',default=date.today)
    end_date = models.DateField('end date',default=date.today)
