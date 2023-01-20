from .models import Productos

def Menu_Link(request):
    links = Productos.objects.all()
    return  dict(links=links)
