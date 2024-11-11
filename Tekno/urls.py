from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("login/", views.logmein, name="login"),
    path("signup/",views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("signin/",views.signin,name="signin"),
    path("monitores/",views.monitores, name="monitores"),
    path("perifericos/", views.perifericos, name="perifericos"),
    path("pc_gaming/", views.pcs, name="pcs"),
    path("about/",views.about, name="about"),
    path("carrito/",views.carrito, name="carrito"),
    
]
