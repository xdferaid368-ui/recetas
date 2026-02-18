from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import FiltroIngredientesForm, IngredienteModelForm, IngredienteForm, IngredienteRecetaModelForm
from django.forms import formset_factory
from django.views.generic import TemplateView ,ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .serializers import RecetaSerializer, IngredienteSerializer
class Inicio(TemplateView):
    template_name = 'app/inicio.html'
    
def inicio(request):
    return render(request, 'app/inicio.html')
class IngredienteCrear(CreateView):
    model = Ingrediente
    form_class = IngredienteModelForm
    template_name = "app/ingrediente_nuevo.html"
    success_url = reverse_lazy('ingredientes')
    def form_valid0(self, form):
        response = super().form_valid(form)
        return response

    def form_invalido(self, form):
        response = super().form_invalid(form)
        return response
    
class IngredienteEditar(UpdateView):
    model = Ingrediente
    form_class = IngredienteModelForm
    template_name = 'app/ingrediente_editar.html'
    success_url = reverse_lazy('ingredientes')

class IngredientesListaView(ListView):
    model = Ingrediente
    template_name = 'app/ingredientes_lista.html'
    context_object_name = 'ingredientes'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        refrigerado = self.request.GET.get('refrigerado')

        if categoria:
            queryset = queryset.filter(categoria_id=categoria)

        if refrigerado:
            queryset = queryset.filter(refrigerado=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = CategoriaIngrediente.objects.all()
        context['refrigerado_filtro'] = self.request.GET.get('refrigerado')
        return context
class IngredientesDetalleView(DetailView):
    model = Ingrediente
    template_name = 'app/ingrediente_detalle.html'
    context_object_name = 'ingrediente'

class IngredienteEliminar(DeleteView):
    model = Ingrediente
    template_name = 'app/confirmar_eliminar.html'
    success_url = reverse_lazy('ingredientes')

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

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer