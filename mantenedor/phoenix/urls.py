"""phoenix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('registrarProducto', include('app.urls')),
    path('listarProducto', include('app.urls')),
    path('listarProducto/<str:producto_marca>', include('app.urls')),
    path('editarProducto/<int:codigo_producto>', include('app.urls')),
    path('borrarProducto/<int:codigo_producto>', include('app.urls')),
    path('paginaPrincipal', include('app.urls')),
    path('accesorios', include('app.urls')),
    path('carcasas', include('app.urls')),
    path('funkos', include('app.urls')),
    path('llaveros', include('app.urls')),
    path('peluches', include('app.urls')),
    path('ropa', include('app.urls')),
    path('tazones', include('app.urls')),
    path('contactenos', include('app.urls')),
    path('entregas', include('app.urls')),
]
