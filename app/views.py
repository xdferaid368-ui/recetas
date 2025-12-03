from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import FiltroIngredientesForm, IngredienteModelForm, IngredienteForm, IngredienteRecetaModelForm
from django.forms import formset_factory

def inicio(request):
    return render(request, 'app/inicio.html')


def ingredientes_lista(request):
    categorias = CategoriaIngrediente.objects.all()
    ingredientes = Ingrediente.objects.all()

    categoria = request.GET.get('categoria')
    refrigerado = request.GET.get('refrigerado')

    if categoria:
        ingredientes = ingredientes.filter(categoria_id=categoria)

    if refrigerado:
        ingredientes = ingredientes.filter(refrigerado=True)

    return render(request, 'app/ingredientes_list.html', {
        'ingredientes': ingredientes,
        'categorias': categorias,
        'refrigerado_filtro': refrigerado,
        'formulario_filtro': FiltroIngredientesForm(),
    })

def ingrediente_nuevo(request):
    IngredienteFormSet = formset_factory(IngredienteForm, extra=4)

    if request.method == 'POST':
        formset = IngredienteFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                datos = form.cleaned_data
                if datos:
                    Ingrediente.objects.create(
                        nombre=datos['nombre'],
                        refrigerado=datos['refrigerado'],
                        categoria_id=datos['categoria'] if datos['categoria'] else None
                    )
            return redirect('ingredientes')
    else:
        formset = IngredienteFormSet()

    return render(request, 'app/ingrediente_nuevo.html', {'formset': formset , 'titulo': 'Crear ingrediente','boton': 'Crear'})

def ingrediente_editar(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == 'POST':
        form = IngredienteModelForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect('ingredientes')
    else:
        form = IngredienteModelForm(instance=ingrediente)

    return render(request, 'app/ingrediente_editar.html', {
        'form': form,
        'titulo': 'Editar ingrediente',
        'boton': 'Guardar cambios'
    })

def ingrediente_eliminar(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == 'POST':
        ingrediente.delete()
        return redirect('ingredientes')

    return render(request, 'app/confirmar_eliminar.html', {
        'ingrediente': ingrediente
    })

def relaciones(request):
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    if request.method == 'POST':
        form = IngredienteRecetaModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = IngredienteRecetaModelForm()  
    else:
        form = IngredienteRecetaModelForm()  
    return render(request, 'app/relaciones.html',{'recetas': recetas,'ingredientes': ingredientes,'form': form })

def receta_lista(request):
    recetas = Receta.objects.all()
    return render(request, 'app/recetas_list.html', {'recetas': recetas})

def receta_detalles(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes = Ingrediente.objects.all()
    return render(request, 'app/receta.html', {'receta': receta, 'ingredientes': ingredientes})

def receta_agregar_ingrediente(request, receta_pk, ingrediente_pk):
    receta = get_object_or_404(Receta, pk=receta_pk)
    ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_pk)
    receta.ingredientes.add(ingrediente)
    return redirect('receta_detalles', pk=receta_pk)

def receta_eliminar_ingrediente(request, receta_pk, ingrediente_pk):
    receta = get_object_or_404(Receta, pk=receta_pk)
    ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_pk)
    receta.ingredientes.remove(ingrediente)
    return redirect('receta_detalles', pk=receta_pk)
