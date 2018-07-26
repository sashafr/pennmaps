from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name = 'home'),
	path('dpsite/', views.mapItem),
    path('webseries/', views.webSeries, name = 'webseries'),
    path('mediagallery/', views.mediaGallery, name = 'mediagallery'),
    path('mediagallery/<slug:tag>/', views.mediaGallery),
    path('archive/search/', views.archiveSearch),
    path('archive/gallery/', views.archiveGallery, name = 'archivegallery'),
    path('archive/gallery/<slug:tag>/', views.archiveGallery),
    path('archive/item/<int:id>/', views.archiveItem, name = 'archiveitem'),
    path('about/team/', views.aboutTeam, name = 'aboutteam'),
    path('about/project/', views.aboutProject, name = 'aboutproject'),
    path('map/', views.map, name = 'map'),
]
