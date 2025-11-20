from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ingredientes', views.ingredientes_lista, name='ingredientes'),
    path('ingrediente/nuevo', views.ingrediente_crud, name='ingrediente_nuevo'),
    path('ingrediente/<int:pk>/editar', views.ingrediente_crud, name='ingrediente_editar'),
    path('ingrediente/<int:pk>/eliminar', views.ingrediente_eliminar, name='confirmar_eliminar'),
]