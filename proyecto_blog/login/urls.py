from django.urls import path
from login import views


urlpatterns = [
    path("ingresar/", views.Ingresar.as_view(), name="ingresar"),
    path("salir/", views.Salir.as_view(), name="salir"),
    path('crear/', views.CrearCuenta.as_view(), name="crear_cuenta"),

]