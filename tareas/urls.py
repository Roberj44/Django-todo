from django.urls import path
from .views import *

urlpatterns = [
    path('tareas/', TareasLista.as_view(), name="tareas"),
    path('tareasdetalles/<int:pk>/', TareasDetalles.as_view(), name="tareasdetalles"),
    path('tareascrear/', TareasCrear.as_view(), name="tareascrear"),
    path('tareasborrar/<int:pk>/', TareasBorrar.as_view(), name="tareasborrar"),
    ]