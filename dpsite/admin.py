from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

admin.site.register(Tag)
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
