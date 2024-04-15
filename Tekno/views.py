from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Producto
from django.db.models import Q



def home(request):
    return render(request,"tekno/index.html")


def products(request):
    return render(request,"tekno/products.html",{
        "errorNeedLogin" : "You must be logged in to view this site!"
    }) 

def logmein(request):

    if request.method == "GET":
        return render(request,"registration/login.html")
    else:
         pass

def signup(request):
    username = request.POST.get("username1")
    email = request.POST.get("email")
    nombre = request.POST.get("firstname")
    apellido = request.POST.get("lastname")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")
    if password1 == password2:
            # register user
        try:
            user = User.objects.create_user(username = username,password = password1,email=email,first_name = nombre,last_name = apellido) 
            user.save()
            login(request,user)
            return redirect("home")
        except:
            return render(request,"registration/login.html",{
                "error" : "ERROR! : User already exists.",
                "alertUser" : "true"
            })
    else:
        return render(request,"registration/login.html",{
            "error" : "ERROR! Password does not match!",
            "alertPass" : "true",
        })
    
def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request,"registration/signin.html")
    else:
        user = authenticate(request,username = request.POST["username1"],password = request.POST["password1"])
        if user is None:
            return render(request,"registration/signin.html",{
                "errorSignin" : "Username or password is incorrect.",
                "alertUser" : "true"
            })
        else:
            login(request,user)
            return redirect("home")
        
def gaming(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()
    print(busqueda)
    
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda)
        ).distinct()
    return render(request,"tekno/gaming.html",{"productos" : productos})
        