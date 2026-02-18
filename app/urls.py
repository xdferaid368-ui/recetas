from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet, IngredienteViewSet

router = DefaultRouter()
router.register(r'recetas', views.RecetaViewSet)
router.register(r'ingredientes', views.IngredienteViewSet)

urlpatterns = [
     path('api/', include(router.urls)),
     path('api-auth/', include('rest_framework.urls')),
     
     path("", views.Inicio.as_view(), name="Inicio"),

    # Ingredientes
    path('ingredientes', views.IngredientesListaView.as_view(), name='ingredientes'),
    path('ingrediente/nuevo', views.IngredienteCrear.as_view(), name='ingrediente_nuevo'),
    path('ingrediente/<int:pk>/editar/', views.IngredienteEditar.as_view(), name='ingrediente_editar'),
    path('ingrediente/<int:pk>/eliminar', views.IngredienteEliminar.as_view(), name='ingrediente_eliminar'),
    path('ingrediente/<int:pk>', views.IngredientesDetalleView.as_view(), name='IngredienteDetalle')
 ,
    # Relaciones
    path('relaciones', views.relaciones, name='relaciones'),

    # Recetas
    path('recetas', views.receta_lista, name='receta_lista'),
    path('receta/<int:pk>', views.receta_detalles, name='receta_detalles'),
    path('receta/<int:receta_pk>/agregar_ingrediente/<int:ingrediente_pk>',
         views.receta_agregar_ingrediente, name='receta_agregar_ingrediente'),
    path('receta/<int:receta_pk>/eliminar_ingrediente/<int:ingrediente_pk>',
         views.receta_eliminar_ingrediente, name='receta_eliminar_ingrediente'),

]
