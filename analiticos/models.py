from django.db import models
from datetime import datetime, date 
# Create your models here.
class Proceso(models.Model):
	proceso = models.CharField(max_length=30, default="", blank=True)
	pkl = models.FileField(upload_to='archivos/modelos/',default="", blank=False)

	def __str__(self):
		return self.proceso

class Archivo(models.Model):
	Excel=models.FileField(upload_to='archivos/excel/')
	Nombre= models.CharField(max_length=100)

	def __str__(self):
		return self.Nombre

	def borrar(self,*args, **kwargs):
		self.Excel.delete()
		super().delete(*args, **kwargs)

class Modelo(models.Model):
	Archivo= models.ForeignKey(Archivo,on_delete=models.CASCADE)
	Proceso= models.ForeignKey(Proceso, on_delete=models.CASCADE)

