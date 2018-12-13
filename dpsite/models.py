from django.contrib.gis.db import models
from datetime import date
import os
from django.urls import reverse
from django.conf import settings
from django.contrib.sites.models import Site

class TagGroup(models.Model):
    title = models.CharField(max_length = 50)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag Group"
        verbose_name_plural = "Tag Groups"

class Tag(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(blank=True, null=True)
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
    date_created = models.DateField('Uploaded', default=date.today)
    file_upload = models.FileField('File Upload', blank=True, null=True)
    file_url = models.URLField('File URL', max_length=200, blank=True, null=True)
    file_iframe = models.CharField('File <iframe>', max_length = 1000, help_text="Please paste in an &lt;iframe&gt; to embed external content. Content must begin with &lt;iframe&gt; and end with &lt;/iframe&gt; ", blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    start_date = models.DateField('Start Date', blank=True, null=True)
    end_date = models.DateField('End Date', blank=True, null=True)
    media_sources = models.CharField('Sources', max_length = 500, blank=True, null=True)
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

    def get_thm_url(self):
        image_ext = ['.jpg', '.jpeg', '.jpe', '.gif', '.png', '.bmp']
        video_ext = ['.mp4', '.webm']
        audio_ext = ['.mp3', '.wav']

        if self.thumbnail:
            return self.thumbnail.url
        elif self.file_upload:
            filename, ext = os.path.splitext(self.file_upload.name)
            if ext in image_ext:
                return self.file_upload.url
            elif ext in video_ext:
                return settings.STATIC_URL + 'img/video_default.png'
            elif ext in audio_ext:
                return settings.STATIC_URL + 'img/video_default.png'
            else:
                return settings.STATIC_URL + 'img/file_default.png'
        else:
            return settings.STATIC_URL + 'img/image_default.png'

    def display_media(self, classes = ""):
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
            return '<a class="'+ classes + '" href="' + self.file_url + '" target="_blank">View File</a>'
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Media File"
        verbose_name_plural = "Media"
        ordering = ['title']

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

    def get_thm_url(self):
        if self.media.count() > 0:
            return self.media.all().order_by('mappedmedia__order')[0].get_thm_url()
        else:
            return settings.STATIC_URL + 'img/image_default.png'

    def display_media_thumb(self):
        if self.media.count() > 0:
            return self.media.all().order_by('mappedmedia__order')[0].display_media_thumb()
        else:
            return '<img class="media-thumb" src="' + settings.STATIC_URL + 'img/image_default.png" alt="' + self.title + '">'

    def display_media_full(self):
        if self.media.count() > 0:
            return self.media.all().order_by('mappedmedia__order')[0].display_media()
        else:
            return '<img class="media-full" src="' + settings.STATIC_URL + 'img/image_default.png" alt="' + self.title + '">'

    def get_pocs(self):
        pocs = PartOfCity.objects.all()
        poc_ids = []
        for poc in pocs:
            if self.location1 and self.location1.intersects(poc.area):
                poc_ids.append(poc.id)
        return poc_ids

    def get_absolute_url(self):
        return reverse('archiveitem', kwargs={'id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Map Item"
        verbose_name_plural = "Map Items"
        ordering = ['title']

class MappedMedia(models.Model):
    map_item = models.ForeignKey(MapItem, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Media"
        ordering = ('order', )

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

    def get_thm_url(self):
        image_ext = ['.jpg', '.jpeg', '.jpe', '.gif', '.png', '.bmp']
        video_ext = ['.mp4', '.webm']
        audio_ext = ['.mp3', '.wav']

        if self.thumbnail:
            return self.thumbnail.url
        elif self.file_upload:
            filename, ext = os.path.splitext(self.file_upload.name)
            if ext in image_ext:
                return self.file_upload.url
            elif ext in video_ext:
                return settings.STATIC_URL + 'img/video_default.png'
            elif ext in audio_ext:
                return settings.STATIC_URL + 'img/video_default.png'
            else:
                return settings.STATIC_URL + 'img/file_default.png'
        else:
            return settings.STATIC_URL + 'img/image_default.png'

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
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Part of City"
        verbose_name_plural = "Parts of City"

class TimePeriod(models.Model):
    title = models.CharField(max_length = 50)
    start_date = models.DateField('start date',default=date.today)
    end_date = models.DateField('end date',default=date.today)

class HomeSlide(models.Model):
    slide_title = models.CharField(max_length = 50)
    slide_text = models.TextField('Slide Text')
    related_image = models.ImageField('Related Image', blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.slide_title

    class Meta:
        verbose_name = "Home Slide"
        verbose_name_plural = "Home Slides"
        ordering = ['order']

class SiteConfig(models.Model):
    site_title = models.CharField('Site Title', max_length = 50)
    site = models.OneToOneField(Site, on_delete=models.CASCADE, primary_key=True,)
    favicon = models.ImageField('Favicon', blank=True, null=True)
    home_sidebar = models.TextField('Home Sidebar', blank=True, null=True)
    aboutproject_main_text = models.TextField('About Project Main Text', blank=True, null=True)
    aboutproject_main_image = models.ImageField('About Project Main Image', blank=True, null=True)
    aboutproject_sidebar_text = models.TextField('About Project Sidebar Text', blank=True, null=True)
    aboutproject_sidebar_image = models.ImageField('About Project Sidebar Image', blank=True, null=True)
    aboutproject_smsidebar_text = models.TextField('About Project Mini-Sidebar Text', blank=True, null=True)
    aboutteam_main_text = models.TextField('About Team Main Text', blank=True, null=True)
    aboutteam_main_image = models.ImageField('About Team Main Image', blank=True, null=True)
    aboutteam_sidebar_text = models.TextField('About Team Sidebar Text', blank=True, null=True)
    aboutteam_sidebar_image = models.ImageField('About Team Sidebar Image', blank=True, null=True)
    aboutteam_smsidebar_text = models.TextField('About Team Mini-Sidebar Text', blank=True, null=True)
    webseries_sidebar = models.TextField('Web Series Sidebar', blank=True, null=True)
    map_sidebar = models.TextField('Map Sidebar', blank=True, null=True)
    footer = models.TextField('Footer', blank=True, null=True)

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"
        ordering = ['site_title']
