from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name = 'base'),
	path('dpsite/', views.mapItem),
    path('webseries/', views.webSeries),
	path('mediaitem/', views.mediaItem), 
]
