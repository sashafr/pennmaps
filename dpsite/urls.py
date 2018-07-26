from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name = 'home'),
	path('dpsite/', views.mapItem),
    path('webseries/', views.webSeries, name = 'webseries'),
	path('media/item/<int:id>/', views.mediaItem, name = 'mediaitem'),
    path('media/gallery/', views.mediaGallery, name = 'mediagallery'),
    path('media/gallery/<slug:tag>/', views.mediaGallery),
    path('archive/search/', views.archiveSearch),
    path('archive/gallery/', views.archiveGallery, name = 'archivegallery'),
    path('archive/gallery/<slug:tag>/', views.archiveGallery),
    path('archive/item/<int:id>/', views.archiveItem),
    path('about/team/', views.aboutTeam, name = 'aboutteam'),
    path('about/project/', views.aboutProject, name = 'aboutproject'),
    path('map/', views.map, name = 'map'),
]
