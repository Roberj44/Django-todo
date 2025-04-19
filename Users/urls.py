from django.urls import path
from .views import *
urlpatterns = [
    path('registro/', registro),
    path('', home), #ESTO DEBE ELIMINAR CUANDO LO VAYA A USAR JUNTO CON EL HTML, AUNQ NO ES NECESARIO
    path('cerrarsesion/', cerrar_sesion),
    path('iniciarsesion/', IniciarSesion),
    ]