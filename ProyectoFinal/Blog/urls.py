from django.contrib import admin
from django.urls import path
from Blog.views import (
    inicio,
    redactores,
    noticias,
    about,
    formularioRedactor,
    formularioComentador,
    formularioModerador,
    busquedaRedactor,
    busquedaComentador,
    busquedaModerador,
)

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("noticias/", noticias, name="Noticias"),
    path("redactores/", redactores, name="Redactores"),
    path("acerca-de/", about, name="Acerca De"),
    path("formulario-redactor", formularioRedactor, name="FormularioRedactor"),
    path("formulario-comentador", formularioComentador, name="FormularioComentador"),
    path("formulario-moderador", formularioModerador, name="FormularioModerador"),
    path("buscar-redactor/", busquedaRedactor, name="Busqueda Redactor"),
    path("buscar-comentador/", busquedaComentador, name="Busqueda Redactor"),
    path("buscar-moderador/", busquedaModerador, name="Busqueda Redactor"),
]
