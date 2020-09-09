from django import forms
from .models import Producto, UserProfile, Categoria

class EditarProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
                'producto_nombre',
                'producto_descripcion',
                'producto_stock',
                'producto_categoria',
                'producto_imagen'
            ]
        labels = {
                 'producto_nombre': 'Nombre',
                 'producto_descripcion': 'Descripcion',
                 'producto_stock': 'Stock',
                 'producto_categoria': 'Categoria',
                 'producto_imagen': 'Imagen'
             }

class EditarCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
                'categoria_nombre',
                'categoria_descripcion',
                'categoria_imagen'
            ]
        labels = {
                 'categoria_nombre': 'Nombre',
                 'categoria_descripcion': 'Descripcion',
                 'categoria_imagen': 'Imagen'
             }

class EditarPerfil(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
                'first_name',
                'last_name',
                'email',
                'fecha_de_nacimiento',
                'ciudad_de_nacimiento',
                'foto',

            ]
        labels = {
                 'first_name': 'Nombre',
                 'last_name': 'Apellidos',
                 'email': 'Correo',
                 'foto': 'Foto de perfil',
             }