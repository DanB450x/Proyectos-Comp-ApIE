from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venta', views.venta, name='venta'),
    path('facturas', views.facturas, name='facturas'),
    path('facturas/<int:id_factura>', views.detalle_factura, name='detalle_factura'),
    path('facturas/<int:id_factura>/eliminar', views.eliminar_factura, name='eliminar_factura'),
]