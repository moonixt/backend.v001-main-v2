from rest_framework import routers, serializers, viewsets
from .models import Usuario




class UsuarioSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Usuario
        fields = ('id','nome','cpf','celular','email',)