from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import forms

from .models import Producto
from .forms import ProductoForm

# Create your views here.

def pagina_principal(request):
    return render(request, 'app/index.html', {})


def accesorios(request):
    return render(request, 'app/accesorios.html', {})


def carcasas(request):
    return render(request, 'app/carcasas.html', {})


def funkos(request):
    return render(request, 'app/funkos.html', {})


def llaveros(request):
    return render(request, 'app/llaveros.html', {})


def peluches(request):
    return render(request, 'app/peluches.html', {})


def ropa(request):
    return render(request, 'app/ropa.html', {})


def tazones(request):
    return render(request, 'app/tazones.html', {})


def contactenos(request):
    return render(request, 'app/contactenos.html', {})


def entregas(request):
    return render(request, 'app/entregas.html', {})


def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/registrarProducto')
    else:
        form = ProductoForm()
        return render(request, "app/ins_producto.html", {'form': form})


def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "app/listar_productos.html", {'productos': productos})


def editar_producto(request, codigo_producto):
    instancia = Producto.objects.get(id=codigo_producto)
    form = ProductoForm(instance=instancia)

    if request.method == "POST":
        form= ProductoForm(request.POST, instance= instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "app/editar_producto.html",{'form':form})


def borrar_producto(request, codigo_producto):
    instancia = Producto.objects.get(id=codigo_producto)
    instancia.delete()
    return redirect("/paginaPrincipal")