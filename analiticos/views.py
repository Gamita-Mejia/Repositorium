from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .models import Archivo
from .forms import formarchivo, formmodelo
from .models import Proceso, Modelo

# Create your views here.
def home (request):

  	return render(request,"analiticos/home.html")

def tutoriales (request): 

  	return render(request, "analiticos/tutoriales.html")

def entrenamiento(request, *args, **kwargs):
    if request.method == 'POST':
        form= formmodelo(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('creacion')
    else:
        form = formmodelo()
    return render(request, 'analiticos/entrenamiento.html', {
        'form': form
    })

    proceso=Proceso.objects.get(pk=pk)
    print(excel)
    return render(request, 'analiticos/creacion.html')

def gestion(request): 

  	return render(request,"analiticos/gestion.html")

def creacion (request, pk):
    excel=Archivo.objects.get(pk=pk)
    proceso=Proceso.objects.get(pk=pk)
    return render (request, "analiticos/creacion.html")

def lista_archivos(request):
    archivos= Archivo.objects.all()
    return render(request, 'analiticos/lista_de_archivos.html', {
        'archivos': archivos
    })


def subir_archivo(request):
    if request.method == 'POST':
        form = formarchivo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_archivos')
    else:
        form = formarchivo()
    return render(request, 'analiticos/subir_archivo.html', {
        'form': form
    })


def borrar_archivo(request,pk):
    if request.method == 'POST':
        archivo = Archivo.objects.get(pk=pk)
        archivo.delete()
    return redirect('lista_archivos')

def seleccion_modelo(request):
    ma=Proceso.objects.all()
    return render(request, 'analiticos/seleccion_modelo.html', {
        'ma': ma
    })

def utilizar_modelo(request, pk):
    if request.method == 'POST':
        modeloelegido=Proceso.objects.get(pk=pk)
        return redirect('lista_archivos')

def utilizar_archivo(request,pk):
    if request.method == 'POST':
        archivoelegido=Archivo.objects.get(pk=pk)
        return redirect('seleccion_modelo')











