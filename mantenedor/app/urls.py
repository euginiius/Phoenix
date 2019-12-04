from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# ----- las rutas de la API ---------
urlpatterns = [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += [
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