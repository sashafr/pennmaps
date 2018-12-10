from django import forms
from django.contrib.gis import forms as geoforms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

class TagResource(resources.ModelResource):

    class Meta:
        model = Tag

class TagAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Tag
        fields = '__all__'

class TagAdmin(ImportExportModelAdmin):
    form = TagAdminForm
    list_display = ('title', 'slug', 'tag_group')
    resource_class = TagResource
    search_fields = ['title']

admin.site.register(Tag, TagAdmin)
admin.site.register(TagGroup)
admin.site.register(OverlayGroup)

class MediaAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}), required=False)
    credits = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}), required=False)
    media_sources = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}), required=False)

    class Meta:
        model = Media
        fields = '__all__'

class MediaAdmin(admin.ModelAdmin):
    form = MediaAdminForm
    autocomplete_fields = ['tags']
    search_fields = ['title']
    list_display = ('title', 'description')
    list_filter = ['tags']
    readonly_fields = ['display_media']
    fields = ['display_media', 'title', 'description', 'credits', 'date_created', 'file_upload', 'file_url', 'file_iframe', 'thumbnail', 'tags', 'start_date', 'end_date', 'media_sources']

    def display_media(self, obj):
        return format_html(obj.display_media())
    display_media.short_description = 'Preview'

admin.site.register(Media, MediaAdmin)

class MapItemAdminForm(forms.ModelForm):
    summary = forms.CharField(widget=CKEditorWidget(), required=False)
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    location1 = geoforms.MultiPointField(widget = geoforms.OSMWidget(attrs={'default_lat': 39.9526, 'default_lon': -75.1652, 'default_zoom': 12 }), required=False)
    location2 = geoforms.MultiPolygonField(widget = geoforms.OSMWidget(attrs={'default_lat': 39.9526, 'default_lon': -75.1652, 'default_zoom': 12 }), required=False)
    info_sources = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = MapItem
        fields = '__all__'

class MapItemResource(resources.ModelResource):

    class Meta:
        model = MapItem

class MappedMediaInline(admin.TabularInline):
    model = MappedMedia
    extra = 1
    readonly_fields = ['display_media']
    fields =['display_media', 'media', 'order']

    def display_media(self, obj):
        return format_html(obj.media.display_media())
    display_media.short_description = 'Preview'

class MapItemAdmin(ImportExportModelAdmin):
    form = MapItemAdminForm
    list_display = ('title','summary','status')
    list_filter = ['tags']
    resource_class = MapItemResource
    inlines = (MappedMediaInline, )
    search_fields = ['title']
    autocomplete_fields = ['tags']

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

class HomeSlideAdminForm(forms.ModelForm):
    slide_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HomeSlide
        fields = '__all__'

class HomeSlideAdmin(admin.ModelAdmin):
    form = HomeSlideAdminForm

admin.site.register(HomeSlide, HomeSlideAdmin)

class SiteConfigAdminForm(forms.ModelForm):
    home_sidebar = forms.CharField(label="Home Sidebar", widget=CKEditorWidget(), required = False)
    aboutproject_main_text = forms.CharField(label="About Project Main Text", widget=CKEditorWidget(), required = False)
    aboutproject_sidebar_text = forms.CharField(label="About Project Sidebar Text", widget=CKEditorWidget(), required = False)
    aboutproject_smsidebar_text = forms.CharField(label="About Project Mini-Sidebar Text", widget=CKEditorWidget(), required = False)
    aboutteam_main_text = forms.CharField(label="About Team Main Text", widget=CKEditorWidget(), required = False)
    aboutteam_sidebar_text = forms.CharField(label="About Team Sidebar Text", widget=CKEditorWidget(), required = False)
    aboutteam_smsidebar_text = forms.CharField(label="About Team Mini-Sidebar Text", widget=CKEditorWidget(), required = False)
    webseries_sidebar = forms.CharField(label="Web Series Sidebar", widget=CKEditorWidget(), required = False)
    map_sidebar = forms.CharField(label="Map Sidebar", widget=CKEditorWidget(), required = False)
    footer = forms.CharField(label="Footer", widget=CKEditorWidget(), required = False)

    class Meta:
        model = SiteConfig
        fields = '__all__'

class SiteConfigAdmin(admin.ModelAdmin):
    form = SiteConfigAdminForm

admin.site.register(SiteConfig, SiteConfigAdmin)
