from django.contrib import admin
from .models import MapItem, WebSeries, Media, PartOfCity, TimePeriod


# Register your models here.
admin.site.register(MapItem)
admin.site.register(WebSeries)
admin.site.register(Media)
admin.site.register(PartOfCity)
admin.site.register(TimePeriod)
