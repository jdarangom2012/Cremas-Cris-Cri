from django.shortcuts import render
from productos.models import Productos
def Home(request):
    productos =  Productos.objects.all().filter(Activo=True)

    contenido = {
        'productos' : productos,        
    }

    return render(request, "Home.html", contenido)


