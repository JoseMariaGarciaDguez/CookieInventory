from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.admin import UserAdmin
admin.site.register(UserProfile, UserAdmin)

admin.site.register(Producto)
admin.site.register(Categoria)

