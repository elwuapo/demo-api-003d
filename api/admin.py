from api.models import Componente, Fabricante, Producto
from django.contrib import admin

# Register your models here.
admin.site.register(Fabricante)
admin.site.register(Componente)
admin.site.register(Producto)