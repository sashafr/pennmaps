from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name = 'base'),
	path('dpsite/', views.mapItem),
    path('webseries/', views.webSeries),
<<<<<<< HEAD
	path('mediaitem/', views.mediaItem),
=======
	path('mediaitem/', views.mediaItem), 
>>>>>>> a508754beddb898778b77ea6b7e2cd356f6f27e1
]
