from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CrearUser(UserCreationForm):
    email = forms.EmailField(
        label = "Email",
        required = True,
    )
    model = User
    fields = ["username", "email","password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class CrearSuperUser(UserCreationForm):
    email = forms.EmailField(
        label = "Email",
        required = True,
    )
    model = User
    fields = ["username", "email","password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user