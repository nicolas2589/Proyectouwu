from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente, Soporte, Equipo

admin.site.register(Cliente)
admin.site.register(Soporte)
admin.site.register(Equipo)
