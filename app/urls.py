from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ingredientes', views.ingredientes_lista, name='ingredientes'),
    path('ingrediente/nuevo', views.ingrediente_nuevo, name='ingrediente_nuevo'),
    path('ingrediente/<int:pk>/editar', views.ingrediente_editar, name='ingrediente_editar'),
    path('ingrediente/<int:pk>/eliminar', views.ingrediente_eliminar, name='ingrediente_eliminar'),
    path('relaciones', views.relaciones, name='relaciones'),
    path('recetas', views.recetas_lista, name='recetas_lista'),
    path('receta/<int:pk>', views.receta_detalle, name='receta_detalle'),
    path('receta/<int:receta_pk>/agregar_ingrediente/<int:ingrediente_pk>', views.receta_agregar_ingrediente, name='receta_agregar_ingrediente'),
]