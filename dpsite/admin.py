from django import forms
from django.contrib import admin
#from ckeditor.widgets import CKEditorWidget
from .models import MapItem, WebSeries, Media, PartOfCity, TimePeriod, Tag, TagGroup, OverlayGroup


# Register your models here.

admin.site.register(Tag)
admin.site.register(TagGroup)
admin.site.register(OverlayGroup)
admin.site.register(Media)


class MapItemAdminForm(forms.ModelForm):

    summary = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = MapItem
        fields = '__all__'
class MapItemAdmin(admin.ModelAdmin):
    form = MapItemAdminForm
    list_display = ('title','location_notes','status')
    list_filter = ['tags']

admin.site.register(MapItem, MapItemAdmin)


admin.site.register(WebSeries)
admin.site.register(PartOfCity)
admin.site.register(TimePeriod)
