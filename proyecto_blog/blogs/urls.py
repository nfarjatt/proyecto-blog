from django.urls import path, include
from blogs import views


urlpatterns = [
    path("", views.ListaDeBlogs.as_view(), name="lista_de_blogs"),
    path("crear/", views.CrearBlog.as_view(), name="crear_blog"),
    path("detalle/<pk>/", views.DetalleDeBlog.as_view(), name="detalle_de_blog"),
    path("editar/<pk>/", views.EditarBlog.as_view(), name="editar_blog"),
    path("borrar/<pk>/", views.BorrarBlog.as_view(), name="borrar_blog"),
    path('login/', include('login.urls')),
    
]