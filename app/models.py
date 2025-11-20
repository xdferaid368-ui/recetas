from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_nombre(value):
    if value.lower() == "televisor":
        raise ValidationError("No puedes añadir un televisor tio")
    

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=100)
        
    def __str__(self):
        return self.nombre

class Refrigerado(models.Model):
    es_refrigerado = models.BooleanField(default=False)

    def __str__(self):
        return "Sí" if self.es_refrigerado else "No"

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_caducidad = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE, null=True, blank=True)
    refrigerado = models.BooleanField(default=False)

def clean(self):
    if self.fecha_caducidad and self.fecha_caducidad < date.today():
        raise ValidationError("La fecha no puede ser anterior a hoy")
