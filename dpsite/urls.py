from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name = 'base'),
	path('dpsite/', views.mapItem),
    path('webseries/', views.webSeries, name = 'webseries'),
	path('mediaitem/', views.mediaItem),
	path('mediaitem/', views.mediaItem),
    path('media/gallery/', views.mediaGallery),
    path('media/gallery/<slug:tag>/', views.mediaGallery),
    path('archive/search/', views.archiveSearch),
    path('archive/gallery/', views.archiveGallery),
    path('archive/gallery/<slug:tag>/', views.archiveGallery),
    path('archive/item/<int:id>/', views.archiveItem),
    path('about/team/', views.aboutTeam),
    path('about/project/', views.aboutProject),
    path('map/', views.map),
]
