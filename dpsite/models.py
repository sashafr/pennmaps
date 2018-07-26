from django.contrib.gis.db import models
from datetime import date
import os
from django.urls import reverse
from django.conf import settings

class TagGroup(models.Model):
    title = models.CharField(max_length = 50)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag Group"
        verbose_name_plural = "Tag Groups"

class Tag(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField()
    tag_group = models.ForeignKey('TagGroup', on_delete=models.CASCADE, blank=True, null=True)
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
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200, blank=True, null=True)
    credits = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateField('date', default=date.today)
    file_upload = models.FileField('File Upload', blank=True, null=True)
    file_url = models.URLField('File URL', max_length=200, blank=True, null=True)
    file_iframe = models.CharField('File <iframe>', max_length = 1000, help_text="Please paste in an &lt;iframe&gt; to embed external content. Content must begin with &lt;iframe&gt; and end with &lt;/iframe&gt; ", blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    media_sources = models.CharField('Sources', max_length = 500, blank=True, null=True)

    def display_media(self, classes = ""):
        image_ext = ['.jpg', '.jpeg', '.jpe', '.gif', '.png', '.bmp']
        video_ext = ['.mp4', '.webm']
        audio_ext = ['.mp3', '.wav']

        if self.file_iframe:
            return self.file_iframe
        elif self.file_upload:
            filename, ext = os.path.splitext(self.file_upload.name)
            if ext in image_ext:
                return '<img class="'+ classes + '" src="' + self.file_upload.url + '" alt="' + self.title + '">'
            elif ext in video_ext:
                return '<video class="'+ classes + '" controls><source src="' + self.file_upload.url + '" type="video/' + ext[1:] + '"></video>'
            elif ext in audio_ext:
                return '<audio class="'+ classes + '" controls><source src="' + self.file_upload.url + '" type="audio/' + ext[1:] + '"></audio>'
        else:
            return "to do"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "media"

class MapItem(models.Model):
    title = models.CharField(max_length = 50)
    summary = models.CharField(max_length = 200, blank=True, null=True)
    description = models.CharField(max_length = 5000, blank=True, null=True)
    info_sources = models.CharField(max_length = 2000, blank=True, null=True)
    location_notes = models.CharField(max_length = 50, blank=True, null=True)
    start_date = models.DateField('start date',default=date.today, blank=True, null=True)
    end_date = models.DateField('end date',default=date.today, blank=True, null=True)
    status = models.CharField(max_length = 50, blank=True, null=True)
    location1 = models.MultiPointField(blank=True, null=True)
    location2 = models.MultiPolygonField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    media = models.ManyToManyField('Media', through = 'MappedMedia', blank=True)
    min_zoom = models.IntegerField(blank=True, null=True)
    max_zoom = models.IntegerField(blank=True, null=True)
    overlay_group = models.ManyToManyField('OverlayGroup', blank=True)
    def __str__(self):
        return self.title

class MappedMedia(models.Model):
    map_item = models.ForeignKey(MapItem, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    order = models.IntegerField()

class WebSeries(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 5000, blank=True, null=True)
    upload_date = models.DateField('Uploaded', default=date.today, blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    episode = models.IntegerField(blank=True, null=True)
    file_upload = models.FileField('File Upload', blank=True, null=True)
    file_url = models.URLField('File URL', max_length=1000, blank=True, null=True)
    file_iframe = models.CharField('File <iframe>', max_length = 1000, help_text="Please paste in an &lt;iframe&gt; to embed external content. Content must begin with &lt;iframe&gt; and end with &lt;/iframe&gt; ", blank=True, null=True)
    map_location = models.ManyToManyField('MapItem', blank=True, verbose_name="Map")
    tags = models.ManyToManyField('Tag', blank=True)
    credits = models.CharField(max_length=1000, blank=True, null=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    thumbnail = models.FileField('Thumbnail', blank=True, null=True, help_text="If you are uploading a non-image file or using the File URL or File IFrame options, its recommended you select a thumbnail. If you do not, a default image will be used.")

    def get_main_url(self):
        if self.file_url:
            return self.file_url
        elif self.file_upload:
            return self.file_upload.url
        elif self.file_iframe:
            return "iframe"
        else:
            return ""

    def display_media(self):
        image_ext = ['.jpg', '.jpeg', '.jpe', '.gif', '.png', '.bmp']
        video_ext = ['.mp4', '.webm']
        audio_ext = ['.mp3', '.wav']

        classes = 'media-full'

        if self.file_iframe:
            return self.file_iframe
        elif self.file_upload:
            filename, ext = os.path.splitext(self.file_upload.name)
            if ext in image_ext:
                return '<img class="'+ classes + '" src="' + self.file_upload.url + '" alt="' + self.title + '">'
            elif ext in video_ext:
                return '<video class="'+ classes + '" controls><source src="' + self.file_upload.url + '" type="video/' + ext[1:] + '"></video>'
            elif ext in audio_ext:
                return '<audio class="'+ classes + '" controls><source src="' + self.file_upload.url + '" type="audio/' + ext[1:] + '"></audio>'
        elif self.file_url:
            return '<a class="'+ classes + '" href="' + self.file_url + '" target="_blank">View Episode</a>'
        else:
            return "(None)"

    def display_media_thumb(self):
        image_ext = ['.jpg', '.jpeg', '.jpe', '.gif', '.png', '.bmp']
        video_ext = ['.mp4', '.webm']
        audio_ext = ['.mp3', '.wav']

        classes = 'media-thumb'

        if self.thumbnail:
            return '<img class="'+ classes + '" src="' + self.thumbnail.url + '" alt="' + self.title + '">'
        elif self.file_upload:
            filename, ext = os.path.splitext(self.file_upload.name)
            if ext in image_ext:
                return '<img class="'+ classes + '" src="' + self.file_upload.url + '" alt="' + self.title + '">'
            elif ext in video_ext:
                return '<img class="'+ classes + '" src="' + settings.STATIC_URL + 'img/video_default.png" alt="' + self.title + '">'
            elif ext in audio_ext:
                return '<img class="'+ classes + '" src="' + settings.STATIC_URL + 'img/video_default.png" alt="' + self.title + '">'
            else:
                return '<img class="'+ classes + '" src="' + settings.STATIC_URL + 'img/file_default.png" alt="' + self.title + '">'
        else:
            return '<img class="'+ classes + '" src="' + settings.STATIC_URL + 'img/image_default.png" alt="' + self.title + '">'

    def get_absolute_url(self):
        return reverse('webseries')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Web Series"
        ordering = ['season', 'episode']

class PartOfCity(models.Model):
    title = models.CharField(max_length = 50)
    area = models.MultiPolygonField(default=None, blank=True, null=True)

class TimePeriod(models.Model):
    title = models.CharField(max_length = 50)
    start_date = models.DateField('start date',default=date.today)
    end_date = models.DateField('end date',default=date.today)

class PageText(models.Model):
    text_hook = models.CharField('Text Hook', max_length = 50)
    page_text = models.TextField('Page Text')

    def __str__(self):
        return self.text_hook

    class Meta:
        verbose_name = "Page Text"
        verbose_name_plural = "Page Text"
        ordering = ['text_hook']
