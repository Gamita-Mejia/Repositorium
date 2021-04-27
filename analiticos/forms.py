from django import forms

from .models import Archivo, Proceso, Modelo


class formarchivo(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('Excel','Nombre')



class formmodelo(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ('Archivo', 'Proceso')


