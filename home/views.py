from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .form import FormCreateCliente,FormModifCliente,FormCreateEquipo,FormModifEquipo,FormCreateSoporte,FormModifSoporte
from .models import Cliente, Equipo, Soporte
from django.urls import reverse_lazy
# Create your views here.

class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "ini.html"
    login_url = "login"

# CRUD de Clientes
class VerCliente(LoginRequiredMixin, generic.ListView):
    template_name = "clientes/verclientes.html"
    model = Cliente
    success_url = reverse_lazy("Index")
    login_url = "login"


class EliminarCliente(LoginRequiredMixin, generic.DeleteView):
    template_name = "clientes/eliminar.html"
    model = Cliente
    success_url = reverse_lazy("Index")
    login_url = "login"


class ModificarCliente(LoginRequiredMixin, generic.UpdateView):
    template_name = "clientes/modificarclientes.html"
    model = Cliente
    form_class = FormModifCliente
    success_url = reverse_lazy("Index")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegistrarCliente(LoginRequiredMixin, generic.CreateView):
    template_name = "clientes/registrarclientes.html"
    model = Cliente
    form_class = FormCreateCliente
    success_url = reverse_lazy("Index")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# CRUD de Clientes
class VerEquipo(LoginRequiredMixin, generic.ListView):
    template_name = "equipos/verequipo.html"
    model = Equipo
    success_url = reverse_lazy("Index")
    login_url = "login"


class EliminarEquipo(LoginRequiredMixin, generic.DeleteView):
    template_name = "equipos/eliminar.html"
    model = Equipo
    success_url = reverse_lazy("Index")
    login_url = "login"


class ModificarEquipo(LoginRequiredMixin, generic.UpdateView):
    template_name = "equipos/modificarequipo.html"
    model = Equipo
    form_class = FormModifEquipo
    success_url = reverse_lazy("Index")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegistrarEquipo(LoginRequiredMixin, generic.CreateView):
    template_name = "equipos/registrarequipo.html"
    model = Equipo
    form_class = FormCreateEquipo
    success_url = reverse_lazy("Index")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# CRUD de Soportes
class VerSoporte(LoginRequiredMixin, generic.ListView):
    template_name = "soportes/versoporte.html"
    model = Soporte
    success_url = reverse_lazy("Index")
    login_url = "login"


class EliminarSoporte(LoginRequiredMixin, generic.DeleteView):
    template_name = "soportes/eliminar.html"
    model = Soporte
    success_url = reverse_lazy("Index")
    login_url = "login"


class ModificarSoporte(LoginRequiredMixin, generic.UpdateView):
    template_name = "soportes/modificarsoporte.html"
    model = Soporte
    form_class = FormModifSoporte
    success_url = reverse_lazy("Index")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegistrarSoporte(LoginRequiredMixin, generic.CreateView):
    template_name = "soportes/registrarsoporte.html"
    model = Soporte
    form_class = FormCreateSoporte
    success_url = reverse_lazy("Index")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
