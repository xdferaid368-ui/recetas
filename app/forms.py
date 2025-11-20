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
