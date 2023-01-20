from django.urls import path
from . import views

urlpatterns = [
     path('',views.productos, name='productos'),
     path('<slug:producto_slug>',views.productos_detalle, name='sabores_por_categoria'),
]
