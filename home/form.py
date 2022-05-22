from django import forms
from .models import Cliente, Equipo, Soporte
from django.contrib.auth.forms import UserCreationForm


class FormCreateCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            "Cliente_Nombre",
            "Cliente_Email",
            "Cliente_Phone",
        ]

    def clean_Cliente_Email(self):
        Cliente_Email = self.cleaned_data["Cliente_Email"]
        if Cliente.objects.filter(Cliente_Email=Cliente_Email).exists() :
            raise forms.ValidationError('El email ya esta en uso')
        return Cliente_Email


class FormModifCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            "Cliente_Nombre",
            "Cliente_Email",
            "Cliente_Phone",
        ]


class FormCreateEquipo(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = [
            "Equipo_Marca",
            "Equipo_Modelo",
            "Equipo_SN",
        ]

    def clean_Equipo_SN(self):
        Equipo_SN = self.cleaned_data["Equipo_SN"]
        if Equipo.objects.filter(Equipo_SN=Equipo_SN).exists() :
            raise forms.ValidationError('El SN ya existe')
        return Equipo_SN


class FormModifEquipo(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = [
            "Equipo_Marca",
            "Equipo_Modelo",
            "Equipo_SN",
        ]


class FormCreateSoporte(forms.ModelForm):

    class Meta:
        model = Soporte
        fields = [
            "Soporte_Cliente",
            "Soporte_Equipo",
            "Soporte_Tecnico",
            "Soporte_Problema",
            "Soporte_Comentarios",
            "Soporte_Inicio",
            "Soporte_Final",
            "Soporte_Solucionado",
        ]


class FormModifSoporte(forms.ModelForm):

    class Meta:
        model = Soporte
        fields = [
            "Soporte_Cliente",
            "Soporte_Equipo",
            "Soporte_Tecnico",
            "Soporte_Problema",
            "Soporte_Comentarios",
            "Soporte_Inicio",
            "Soporte_Final",
            "Soporte_Solucionado",
        ]
