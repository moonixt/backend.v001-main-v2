from rest_framework import routers, serializers, viewsets
from .models import Usuario
from .models import Produto




class UsuarioSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = Usuario
        fields = ('id','nome','cpf','celular','email',)
        
         
        
class ProdutoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Produto
        fields = ('id','image','nome_produto','valor','qtd_estoque','descricao', 'categoria',)