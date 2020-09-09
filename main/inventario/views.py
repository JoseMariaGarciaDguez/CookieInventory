from django.http import HttpResponse
from django.template import loader

from .forms import EditarProducto, EditarPerfil, EditarCategoria
from .models import Producto
from .models import Categoria
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import *
from django.contrib.auth import get_user_model
User = get_user_model()

def inventario(request):
    productos_actuales = Producto.objects.order_by("id")
    plantilla = loader.get_template('inventario/index.html')
    context = {
        'productos_actuales':productos_actuales,
    }
    #salida = ', '.join([p.producto_nombre for p in productos_actuales])
    return HttpResponse(plantilla.render(context,request))

def producto(request,producto_id):
    respuesta = Producto.objects.get(id=Producto.producto_id)
    return HttpResponse(respuesta.producto_stock)

def categoria(request):
    categorias_actuales = Categoria.objects.order_by("id")
    plantilla = loader.get_template('categoria/categorias.html')
    context = {
        'categorias_actuales': categorias_actuales,
    }
    return HttpResponse(plantilla.render(context, request))
def VerCategoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id);
    productos_filtrados = Producto.objects.filter(producto_categoria_id=categoria_id)
    plantilla = loader.get_template("categoria/ver_categoria/productos_categoria.html")
    context = {
        'productos_filtrados':productos_filtrados,
        'categoria':categoria,
    }
    return HttpResponse(plantilla.render(context,request))

class VerPerfil(UpdateView):
    template_name = "perfil/ver_perfil/perfil.html"
    form_class = EditarPerfil
    success_url = reverse_lazy('index')
    queryset = User.objects.all()
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class RegistroUsuario(CreateView):
    model = User
    template_name = "registro/registrar.html"
    form_class = UserCreationForm
    success_url = "registration/registration.html"

class EditarProducto(UpdateView):
    template_name = "producto/editar_producto/editar.html"
    form_class = EditarProducto
    success_url = reverse_lazy('index')
    queryset = Producto.objects.all()
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class EditarCategoria(UpdateView):
    template_name = "categoria/editar_categoria/editar_categoria.html"
    form_class = EditarCategoria
    success_url = reverse_lazy('index')
    queryset = Categoria.objects.all()
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('index')
    template_name = "producto/borrar_producto/eliminar.html"

class EliminarCategoria(DeleteView):
    model = Categoria
    success_url = reverse_lazy('index')
    template_name = "categoria/eliminar_categoria/eliminar_categoria.html"
