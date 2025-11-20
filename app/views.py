from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingrediente, CategoriaIngrediente
from .forms import *
# Create your views here.
def inicio(request):
    pass


def ingredientes_lista(request):
    categorias = CategoriaIngrediente.objects.all()
    categoria_seleccionada = request.GET.get('categoria')
    refrigerado_filtro = request.GET.get('refrigerado')

    ingredientes = Ingrediente.objects.all()

    if categoria_seleccionada:
        ingredientes = ingredientes.filter(categoria_id=categoria_seleccionada)

    if refrigerado_filtro:
        ingredientes = ingredientes.filter(refrigerado=True)

    formulario_filtro = FiltroIngredientesForm()
    
    return render(request, 'app/ingredientes_lista.html', {
        'ingredientes': ingredientes,
        'categorias': categorias,
        'refrigerado_filtro': refrigerado_filtro,
        'formulario_filtro': formulario_filtro,
    })
def ingrediente_eliminar(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('ingredientes')
    return render(request, 'app/confirmar_eliminar.html', {'ingrediente': ingrediente})
def ingrediente_nuevo(request):
    print(request)
    if request.method == 'POST':
        form = IngredienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingrediente')
    else:
        form = IngredienteModelForm()
    estado = 'crear'
    return render(request, 'blog/ingrediente_nuevo.html', {'form': form, 'estado': estado})

def ingrediente_crud(request, pk=None):
    """
    Función para crear o editar un autor.
    Si pk es None -> crear
    Si pk tiene valor -> editar
    """
    if pk:  
        ingrediente = get_object_or_404(Ingrediente, pk=pk)
        estado = 'editar'
    else: 
        ingrediente = None
        estado = 'crear'
    
    if request.method == 'POST':
        form = IngredienteModelForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect('ingredientes')
    else:
        form = IngredienteModelForm(instance=ingrediente)
    categorias = CategoriaIngrediente.objects.all()
    return render(request, 'app/ingrediente_crud.html', {
        'form': form,
        'estado': estado,
        'categorias': categorias
    })