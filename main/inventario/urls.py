from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from .views import EditarProducto, EliminarProducto, VerCategoria, VerPerfil, EditarCategoria, EliminarCategoria

from . import views

urlpatterns = [
    path('', views.inventario, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<int:categoria_id>/', VerCategoria,name='categoria'),
    path('categoria/', views.categoria, name='categorias'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('editar/<int:pk>/', EditarProducto.as_view(), name='editar'),
    path('editar_categoria/<int:pk>/', EditarCategoria.as_view(), name='editar_categoria'),
    path('eliminar/<int:pk>/', EliminarProducto.as_view(), name='eliminar'),
    path('eliminar_categoria/<int:pk>/', EliminarCategoria.as_view(), name='eliminar_categoria'),
    path('perfil/<int:pk>', VerPerfil.as_view(), name='perfil'),

]