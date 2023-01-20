from django.contrib import admin
from .models import  Productos

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Nombre_Producto',)}
    list_display = ('Nombre_Producto', 'slug')
    search_fields = (
        'Nombre_Producto',
    )


admin.site.register(Productos, ProductosAdmin)

