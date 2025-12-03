from django import forms 
from .models import *

class FiltroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'refrigerado', 'categoria']

class IngredienteModelForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'refrigerado', 'categoria']

class IngredienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    categoria = forms.CharField(required=True)
    refrigerado = forms.BooleanField(required=False)


class IngredienteRecetaModelForm(forms.ModelForm):
    class Meta:
        model = IngredienteReceta
        fields = ['receta' ,'ingrediente', 'cantidad', 'medida']