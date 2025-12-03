from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_nombre(value):
    if value.lower() == "televisor":
        raise ValidationError("No puedes añadir un televisor tío")
    

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Refrigerado(models.Model):
    es_refrigerado = models.BooleanField(default=False)

    def __str__(self):
        return "Sí" if self.es_refrigerado else "No"

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField('Ingrediente', through='IngredienteReceta')
    def __str__(self):
        return self.nombre
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_caducidad = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE, null = True)
    refrigerado = models.BooleanField(default=False)
    cantidad = models.FloatField(null=True, blank=True)   
    precio = models.FloatField(null=True, blank=True) 
    def __str__(self):
        return self.nombre
    def clean(self):
        if self.fecha_caducidad and self.fecha_caducidad < date.today():
            raise ValidationError("La fecha no puede ser anterior a hoy")

class IngredienteReceta(models.Model):
    class MedidasChoices(models.TextChoices):
        LITROS = 'L', 'Litros'
        KILOS = 'KG', 'Kilogramos'
        GRAMOS = 'g', 'Gramos'
        UNIDADES = 'UD','Unidades'
        MILILITROS = 'ml','Mililitros'
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    medida = models.CharField(max_length=2, choices= MedidasChoices.choices)