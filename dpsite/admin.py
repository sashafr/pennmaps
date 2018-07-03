from django import forms
from django.contrib.gis import forms as geoforms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import MapItem, WebSeries, Media, PartOfCity, TimePeriod, Tag, TagGroup, OverlayGroup


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
admin.site.register(Media)


class MapItemAdminForm(forms.ModelForm):
    summary = forms.CharField(widget=CKEditorWidget(), required=False)
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    location1 = geoforms.MultiPointField(widget = geoforms.OSMWidget(attrs={'default_lat': 39.9526, 'default_lon': -75.1652, 'default_zoom': 12 }), required=False)
    location2 = geoforms.MultiPolygonField(widget = geoforms.OSMWidget(attrs={'default_lat': 39.9526, 'default_lon': -75.1652, 'default_zoom': 12 }), required=False)

    class Meta:
        model = MapItem
        fields = '__all__'
<<<<<<< HEAD
class MapItemAdmin(admin.ModelAdmin):
=======

class MapItemResource(resources.ModelResource):

    class Meta:
        model = MapItem

class MappedMediaInline(admin.TabularInline):
    model = MappedMedia
    extra = 1

class MapItemAdmin(ImportExportModelAdmin):
>>>>>>> 292ca76adc9aa97a7c52e5a363b22c5395e4e82f
    form = MapItemAdminForm
    list_display = ('title','location_notes','status')
    list_filter = ['tags']
    resource_class = MapItemResource
    inlines = (MappedMediaInline, )

admin.site.register(MapItem, MapItemAdmin)


admin.site.register(WebSeries)
admin.site.register(PartOfCity)
admin.site.register(TimePeriod)
