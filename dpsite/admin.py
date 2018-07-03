from django import forms
from django.contrib.gis import forms as geoforms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class TagResource(resources.ModelResource):

    class Meta:
        model = Tag

class TagAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'tag_group')
    resource_class = TagResource

admin.site.register(Tag, TagAdmin)
admin.site.register(TagGroup)
admin.site.register(OverlayGroup)

class MediaAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=False)
    credits = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Media
        fields = '__all__'

class MediaResource(resources.ModelResource):

    class Meta:
        model = Media

class MediaAdmin(ImportExportModelAdmin):
    form = MediaAdminForm
    list_display = ('title', 'description')
    resource_class = MediaResource

admin.site.register(Media, MediaAdmin)

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

admin.site.register(MapItem, MapItemAdmin)

admin.site.register(WebSeries)
admin.site.register(PartOfCity)
admin.site.register(TimePeriod)
