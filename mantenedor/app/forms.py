from django import forms
from .models import Producto, DatosCliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'modelo', 'descripcion', 'stock','imagen']

class DatosClienteForm(forms.ModelForm):
    class Meta:
        model = DatosCliente
        fields = ['region', 'comuna', 'nombre_cliente', 'email', 'telefono', 'tipo_vivienda', 'rut', 'fecha_nacimiento', 'direccion']