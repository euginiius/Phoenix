from .models import Producto
from rest_framework import serializers

# esta clase nos va a permitir la 
# conversion del objeto a json y viceversa

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'