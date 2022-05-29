from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .form import FormCreateCliente,FormModifCliente,FormCreateEquipo,FormModifEquipo,FormCreateSoporte,FormModifSoporte
from .models import Cliente, Equipo, Soporte
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db import connection
from django.db.utils import OperationalError
from .serializer import ClienteSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

#api de auth usuario
@api_view(['GET'])
def login(request):
    user=request.GET['User']
    pwd=request.GET['Pwd']
    user = authenticate(username=user, password=pwd)
    if user is not None:
        token=Token.objects.get_or_create(user=user)
        return Response({'Token':str(token[0])})
    else:
        return Response(['Error usuario o contraseña incorrectos'])

# Apis de historial
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historial_equipo(request,pk):
    cursor = connection.cursor()
    try:
        cursor.callproc("historial_equipo",[pk])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historial_cliente(request, pk):
    cursor = connection.cursor()
    try:
        cursor.callproc("historial_cliente",[pk])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historial_tecnico(request, pk):
    cursor = connection.cursor()
    try:
        cursor.callproc("historial_tecnico",[pk])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)
#apis para crear
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crear_cliente(request):
    nombre=request.GET['Nombre']
    email=request.GET['Email']
    tel=request.GET['Tel']
    cursor = connection.cursor()
    try:
        cursor.callproc("insert_cliente",[nombre,email,tel])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crear_equipo(request):
    marca=request.GET['Marca']
    modelo=request.GET['Modelo']
    sn=request.GET['SN']
    cursor = connection.cursor()
    try:
        cursor.callproc("insert_equipo",[marca, modelo, sn])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crear_soporte(request):
    problema =request.GET['Problema']
    comentarios=request.GET['Comentarios']
    tecnico_id=request.GET['Tecnico_id']
    equipo_id=request.GET['Equipo_id']
    cliente_id=request.GET['Cliente_id']

    cursor = connection.cursor()
    try:
        cursor.callproc("crear_soporte", [problema, comentarios, tecnico_id, equipo_id, cliente_id])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)
#api para cerrar soporte
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cerrar_soporte(request,pk):
    cierre = request.GET['Cierre']
    cursor = connection.cursor()
    try:
        cursor.callproc("cerrar_soporte", [pk, cierre])
        res = cursor.fetchall()
        print(res)
    finally:
        cursor.close()
    return Response(res)
#api para actualizar
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def act_cliente(request,pk):
    nombre=request.GET['Nombre']
    email=request.GET['Email']
    tel=request.GET['Tel']
    cursor = connection.cursor()
    try:
        cursor.callproc("act_cliente", [pk, nombre, email, tel])
        res = cursor.fetchall()
        print(res)
    except OperationalError as e:
        return Response([str(e)])

    finally:
        cursor.close()
    return Response(res)
#index
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
