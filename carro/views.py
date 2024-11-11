from django.shortcuts import render

from .carro import Cart
from Tekno.models import Producto
from django.shortcuts import redirect

def agregar_producto(request, producto_id):
    carro = Cart(request)
    producto = Producto.objects.get(id_producto = producto_id)
    carro.add(producto)
    return redirect("carrito")

def guardar_carrito(request):
    carro = Cart(request)
    carro.save()
    return redirect("carrito")
    

def eliminar_producto(request, producto_id):
    carro = Cart(request)
    producto = Producto.objects.get(id_producto = producto_id)
    carro.remove(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carro = Cart(request)
    producto = Producto.objects.get(id_producto = producto_id)
    carro.decrement(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carro = Cart(request)
    carro.clear()
    return redirect("carrito")
