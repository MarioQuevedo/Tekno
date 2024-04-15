from django.db import models
from django.contrib.auth.models import User

    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100,null = False)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length = 100,null = False)
    tipo = models.CharField(max_length=100, null=False,default=False)
    stock = models.IntegerField(default="0")
    precio = models.FloatField(default = False, null = False)
    imagen = models.ImageField(upload_to="static/imagenes")
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE ,blank= True)
    nombre = User.username
    apellido1 = models.CharField(max_length = 15,null = False)
    apellido2 = models.CharField(max_length = 15,null = False)
    fecha_nacimiento = models.DateField(null = False)
    cp = models.CharField(max_length = 5,null = False)
    dni = models.CharField(max_length = 9,null = False)
    sexo = models.Choices