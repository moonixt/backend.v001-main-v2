from rest_framework import routers, serializers, viewsets
from .models import Usuario
from .models import Produto
from .models import Restaurante




class UsuarioSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = Usuario
        fields = ('id','nome','cpf','celular','email',)
        
        
class RestauranteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Restaurante
        fields = ('id','image','nome_restaurante','logradouro_restaurante','numero_restaurante','complemento_restaurante', 'ponto_ref_restaurante',
                  'bairro_restaurante', 'cidade_restaurante', 'uf_restaurante', 'cep_restaurante', 'descricao')
        
         
        
class ProdutoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Produto
        fields = ('id','image','nome_produto','valor','qtd_estoque','descricao', 'categoria',)