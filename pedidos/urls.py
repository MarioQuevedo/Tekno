from django.urls import path
from . import views

app_name = "pedido"
urlpatterns = [
    path("",views.procesar_pedido,name = "procesar_pedido"),
]