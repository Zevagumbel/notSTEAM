from django.contrib import admin
from .models import Genero, Juego, Desarrollador, Editor

# Register your models here.
admin.site.register(Genero)
admin.site.register(Juego)
admin.site.register(Desarrollador)
admin.site.register(Editor)