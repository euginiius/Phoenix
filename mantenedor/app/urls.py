from django.urls import path, include
from . import views

urlpatterns = [
    path('registrarProducto', views.registrar_producto),
    path('listarProducto', views.listar_productos),
    path('listarProducto/<str:producto_marca>', views.listar_marca),
    path('editarProducto/<int:codigo_producto>', views.editar_producto),
    path('borrarProducto/<int:codigo_producto>', views.borrar_producto),
    path('paginaPrincipal', views.pagina_principal),
    path('accesorios', views.accesorios),
    path('carcasas', views.carcasas),
    path('funkos', views.funkos),
    path('llaveros', views.llaveros),
    path('peluches', views.peluches),
    path('ropa', views.ropa),
    path('tazones', views.tazones),
    path('contactenos', views.contactenos),
    path('entregas', views.entregas),

]