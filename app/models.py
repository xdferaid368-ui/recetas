from django.db import models

# Create your models here.

""" class CategoriaChoices(models.TextChoices):
    LEGUMBRE = "LE", "Legrumbres" """
    

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey("CategoriaIngrediente",on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre}, Categoria = {self.categoria}'