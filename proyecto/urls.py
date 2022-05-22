"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Index
    path('', views.Index.as_view(),name='Index'),
    # Urls de autentificacion
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="login.html"), name="logout"),
    # Url para el Crud de Clientes
    path('registrarcliente/', views.RegistrarCliente.as_view(), name='registrarC'),
    path('verclientes/', views.VerCliente.as_view(), name='verC'),
    path('modificarclientes/<int:pk>/', views.ModificarCliente.as_view(), name='modificarC'),
    path('eliminarclientes/<int:pk>/', views.EliminarCliente.as_view(), name='eliminarC'),
    # Url para el Crud de Equipos
    path('registrarequipo/', views.RegistrarEquipo.as_view(), name='registrarE'),
    path('verequipo/', views.VerEquipo.as_view(), name='verE'),
    path('modificarequipo/<int:pk>/', views.ModificarEquipo.as_view(), name='modificarE'),
    path('eliminarequipo/<int:pk>/', views.EliminarEquipo.as_view(), name='eliminarE'),
    # Url para el Crud de Soporte
    path('registrarsoporte/', views.RegistrarSoporte.as_view(), name='registrarS'),
    path('versoporte/', views.VerSoporte.as_view(), name='verS'),
    path('modificarsoporte/<int:pk>/', views.ModificarSoporte.as_view(), name='modificarS'),
    path('eliminarsoporte/<int:pk>/', views.EliminarSoporte.as_view(), name='eliminarS'),

]
