from django import forms
from .models import Tareas

class TareaCrearForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ["titulo", "descripcion"]