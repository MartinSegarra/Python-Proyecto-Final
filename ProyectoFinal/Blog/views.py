from django.shortcuts import render
from Blog.forms import (
    FormularioRedactor,
    FormularioComentador,
    FormularioModerador,
    Buscar,
)
from Blog.models import Redactor, Comentador, Moderador

# Create your views here.


def inicio(request):
    return render(request, "Blog/index.html")


def noticias(request):
    return render(request, "Blog/noticias.html")


def redactores(request):
    return render(request, "Blog/redactores.html")


def about(request):
    return render(request, "Blog/about.html")


def formularioRedactor(request):
    if request.method == "POST":
        myFormRedactor = FormularioRedactor(request.POST)

        if myFormRedactor.is_valid():
            data = myFormRedactor.cleaned_data
            redactor = Redactor(
                nombre=data["nombre"], email=data["email"], edad=data["edad"]
            )
            redactor.save()
            return render(request, "Blog/index.html")

    else:
        myFormRedactor = FormularioRedactor()

    return render(
        request, "Blog/formularioRedactor.html", {"myFormRedactor": myFormRedactor}
    )


def formularioComentador(request):
    if request.method == "POST":
        myFormComentador = FormularioComentador(request.POST)

        if myFormComentador.is_valid():
            data = myFormComentador.cleaned_data
            comentador = Comentador(
                nombre=data["nombre"], email=data["email"], edad=data["edad"]
            )
            comentador.save()
            return render(request, "Blog/index.html")

    else:
        myFormComentador = FormularioComentador()

    return render(
        request,
        "Blog/formularioComentador.html",
        {"myFormComentador": myFormComentador},
    )


def formularioModerador(request):
    if request.method == "POST":
        myFormModerador = FormularioModerador(request.POST)

        if myFormModerador.is_valid():
            data = myFormModerador.cleaned_data
            moderador = Moderador(nombre=data["nombre"], email=data["email"])
            moderador.save()
            return render(request, "Blog/index.html")

    else:
        myFormModerador = FormularioModerador()

    return render(
        request,
        "Blog/formularioModerador.html",
        {"myFormModerador": myFormModerador},
    )


def busquedaRedactor(request):
    if request.method == "POST":
        mySearchRedactor = Buscar(request.POST)
        if mySearchRedactor.is_valid():
            data = mySearchRedactor.cleaned_data
            redactores = Redactor.objects.filter(nombre__icontains=data["nombre"])

            return render(
                request, "Blog/search_results.html", {"resultados": redactores}
            )

    else:
        mySearchRedactor = Buscar()

    return render(
        request, "blog/busquedaRedactor.html", {"mySearchRedactor": mySearchRedactor}
    )


def busquedaComentador(request):
    if request.method == "POST":
        mySearchComentador = Buscar(request.POST)
        if mySearchComentador.is_valid():
            data = mySearchComentador.cleaned_data
            comentadores = Comentador.objects.filter(nombre__icontains=data["nombre"])

            return render(
                request, "Blog/search_results.html", {"resultados": comentadores}
            )

    else:
        mySearchComentador = Buscar()

    return render(
        request,
        "blog/busquedaComentador.html",
        {"mySearchComentador": mySearchComentador},
    )


def busquedaModerador(request):
    if request.method == "POST":
        mySearchModerador = Buscar(request.POST)
        if mySearchModerador.is_valid():
            data = mySearchModerador.cleaned_data
            moderadores = Moderador.objects.filter(nombre__icontains=data["nombre"])

            return render(
                request, "Blog/search_results.html", {"resultados": moderadores}
            )

    else:
        mySearchModerador = Buscar()

    return render(
        request,
        "blog/busquedaModerador.html",
        {"mySearchModerador": mySearchModerador},
    )
