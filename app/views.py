from django.shortcuts import render
from .models import Ingrediente
# Create your views here.
def inicio(request):
    pass

def ingredientes_lista(request):
    filtrar = request.GET.get('filtrar', '')  # Obtener valor de ?filtrar=algo
    if filtrar:
        ingredientes = Ingrediente.objects.filter(nombre__icontains=filtrar)
    else:
        ingredientes = Ingrediente.objects.all()
    return render(request, 'app/ingredientes_lista.html', {'ingredientes': ingredientes, 'filtrar': filtrar})