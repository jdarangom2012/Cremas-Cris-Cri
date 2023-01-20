from django.db import models
from django.urls import reverse

# Create your models here.
class Productos(models.Model):
    Nombre_Producto = models.CharField(max_length=200,unique=True)
    slug = models.CharField(max_length=200,unique=True)
    Descripcion = models.TextField(max_length=200,unique=True)
    Precio = models.IntegerField()
    Imagen = models.ImageField(upload_to='photos/productos')
    stock = models.IntegerField()
    Activo = models.BooleanField(default=True)
    Fecha_Creacion = models.DateField(auto_now_add=True)
    Fecha_Modificacion = models.DateField(auto_now=True)


    #class Meta:
    #    verbose_name  = 'Productos'
    #    verbose_name_plural = 'Productos'
    

    def get_url(self):
        return reverse('sabores_por_categoria',args=[self.slug])

    def __str__(self):
        return self.Nombre_Producto
        