from django.contrib import admin
from django.urls import path
from analiticos import views

urlpatterns = [
    path('',views.home, name='menu'),
    path('tutoriales/',views.tutoriales,name='tutoriales'),
    path('entrenamiento/',views.entrenamiento,name='entrenamiento'),
    path('gestion/',views.gestion, name="gestion"), 
    path('subir_arhivo',views.subir_archivo, name= 'subir_archivo'),
    path('lista_de_archivos',views.lista_archivos, name= 'lista_archivos'),
    path('archivos/<int:pk>/', views.borrar_archivo, name='borrar_archivo'),
    path('proceso/<int:pk>/', views.creacion, name='creacion'),
    path('excel/<int:pk>/', views.creacion, name='creacion'),
    path('seleccion_modelo',views.seleccion_modelo, name= 'seleccion_modelo'), 
    path('utilizar_modelo/<int:pk>/', views.utilizar_modelo, name='utilizar_modelo'),
    path('archivoelegido/<int:pk>/', views.utilizar_archivo, name='utilizar_archivo'),
    path('creacion', views.creacion, name='creacion'),
]
