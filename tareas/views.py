from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

class TareasLista(LoginRequiredMixin, ListView):
    model = Tareas
    context_object_name = "tareas"
    template_name = "lista_tareas.html"

    def get_queryset(self):
        return Tareas.objects.filter(usuario=self.request.user)
    
class TareasDetalles(LoginRequiredMixin, DetailView):
    model = Tareas
    context_object_name = "tarea"
    template_name = "detalles_tarea.html"

class TareasCrear(LoginRequiredMixin, CreateView):
    model = Tareas
    form_class = TareaCrearForm
    template_name = "tareascrear.html"
    success_url = reverse_lazy("tareas")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TareasBorrar(LoginRequiredMixin, DeleteView):
    model = Tareas
    template_name = "tareasborrar.html"
    success_url = reverse_lazy("tareas")