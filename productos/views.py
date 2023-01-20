from django.shortcuts import render, get_object_or_404
from .models import Productos

# Create your views here.
def productos(request):
    sabores =  Productos.objects.all().filter(Activo=True)
    cuantos_sabores = sabores.count()

    datos_sabores = {
        'sabores': sabores,
        'cuantos_sabores': cuantos_sabores
    }

    return render(request, "productos/productos.html",datos_sabores)

def productos_detalle(request, producto_slug):

    try:
        sabor_seleccionado = Productos.objects.get(slug = producto_slug)
    except Exception as e:
        raise e

    contenido = { #objeto
        'sabor_seleccionado' : sabor_seleccionado,
    }

    return render(request, 'productos/productos_detalle.html', contenido)
    
