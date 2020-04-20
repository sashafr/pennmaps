from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('webseries/', views.webSeries, name = 'webseries'),
    path('mediagallery/', views.mediaGallery, name = 'mediagallery'),
    path('mediagallery/<slug:tag>/', views.mediaGallery, name = 'mediagallerytag'),
    path('archive/search/', views.archiveSearch, name = 'search'),
    path('archive/gallery/', views.archiveGallery, name = 'archivegallery'),
    path('archive/gallery/<slug:tag>/', views.archiveGallery, name = 'archivegallerytag'),
    path('archive/item/<int:id>/', views.archiveItem, name = 'archiveitem'),
    path('about', views.aboutTeam, name='about'),
    path('about/team/', views.aboutTeam, name = 'aboutteam'),
    path('about/project/', views.aboutProject, name = 'aboutproject'),
    path('map/', views.map, name = 'map'),
    path('mapall/', views.mapall, name = 'mapall'),
    path('featured/', views.featured, name='featured'),
    path('allitems/', views.allitems, name='allitems'),
]
