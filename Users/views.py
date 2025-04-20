from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *

# Create your views here.

def home(request): #ESTO DEBE ELIMINAR CUANDO LO VAYA A USAR JUNTO CON EL HTML, AUNQ NO ES NECESARIO
    if request.user.is_authenticated:
        return redirect ("/tareas/tareas/")
    else:
        return redirect("/iniciarsesion/")

def registro(request):
    form = CrearUser()
    if request.method=="POST":
        form = CrearUser(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("/") #ESTO DEBE CAMBIAR DONDE LO VAYA A USAR
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro.html", {"form":form})
    else:
        return render(request, "registro.html", {"form":form})


def cerrar_sesion(request):
    logout(request)
    return redirect("/iniciarsesion/") #ESTO DEBE CAMBIAR DONDE LO VAYA A USAR


def IniciarSesion(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("/") #ESTO DEBE CAMBIAR DONDE LO VAYA A USAR
            else:
                messages.error(request, "El usuario no existe")
        else:
            messages.error(request, "Información Incorrecta")
    form = AuthenticationForm()
    return render(request, "iniciarsesion.html", {"form":form})

def crearSuperUser(request):
    form = CrearSuperUser()
    if request.method=="POST":
        form = CrearSuperUser(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect("/admin/") #ESTO DEBE CAMBIAR DONDE LO VAYA A USAR
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "crearsuperuser.html", {"form":form})
    else:
        return render(request, "crearsuperuser.html", {"form":form})