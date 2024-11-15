from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, LineaPedido
from carro.carro import Cart
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url = "/tekno/signin")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Cart(request)
    lineas_pedido = list()
    for key, value in carro.cart.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id = key,
            cantidad = value["quantity"],
            user = request.user,
            pedido=pedido
            
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    
    messages.success(request,"Pedido creado correctamente")
    return redirect("/tekno/home")

