from django import forms
from django.contrib.gis import forms as geoforms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html


# Register your models here.

class TagResource(resources.ModelResource):

    class Meta:
        model = Tag

class TagAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'tag_group')
    resource_class = TagResource
    search_fields = ['title']

admin.site.register(Tag, TagAdmin)
admin.site.register(TagGroup)
admin.site.register(OverlayGroup)
admin.site.register(Media)

class MapItemAdminForm(forms.ModelForm):
    summary = forms.CharField(widget=CKEditorWidget(), required=False)
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    location1 = geoforms.MultiPointField(widget = geoforms.OSMWidget(attrs={'default_lat': 39.9526, 'default_lon': -75.1652, 'default_zoom': 12 }), required=False)
    location2 = geoforms.MultiPolygonField(widget = geoforms.OSMWidget(attrs={'default_lat': 39.9526, 'default_lon': -75.1652, 'default_zoom': 12 }), required=False)

    class Meta:
        model = MapItem
        fields = '__all__'

class MapItemResource(resources.ModelResource):

    class Meta:
        model = MapItem

class MappedMediaInline(admin.TabularInline):
    model = MappedMedia
    extra = 1

class MapItemAdmin(ImportExportModelAdmin):
    form = MapItemAdminForm
    list_display = ('title','location_notes','status')
    list_filter = ['tags']
    resource_class = MapItemResource
    inlines = (MappedMediaInline, )
    search_fields = ['title']

admin.site.register(MapItem, MapItemAdmin)

class WebSeriesAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}), required=False)

    class Meta:
        model = WebSeries
        fields = '__all__'

class WebSeriesAdmin(admin.ModelAdmin):
    form = WebSeriesAdminForm
    autocomplete_fields = ['map_location', 'tags']
    search_fields = ['title']
    list_display = ('season', 'episode', 'title', 'description')
    list_display_links = ('title', )
    list_filter = ['tags']
    readonly_fields = ['display_media']
    fields = ['display_media', 'title', 'description', 'upload_date', 'season', 'episode', 'file_upload', 'file_url', 'file_iframe', 'thumbnail', 'map_location', 'tags', 'credits', 'start_date', 'end_date']
    view_on_site = True

    def display_media(self, obj):
        return format_html(obj.display_media())
    display_media.short_description = 'Preview'

admin.site.register(WebSeries, WebSeriesAdmin)

admin.site.register(PartOfCity)
admin.site.register(TimePeriod)

class PageTextAdminForm(forms.ModelForm):
    page_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PageText
        fields = '__all__'

class PageTextAdmin(admin.ModelAdmin):
    form = PageTextAdminForm

admin.site.register(PageText, PageTextAdmin)
