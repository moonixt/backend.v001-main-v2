from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .auth import generate_otp, send_otp_phone
from .models import Produto, Usuario, Restaurante, Endereco, Pedido
from .serializers import ProdutoSerializer, UsuarioSerializer, RestauranteSerializer, EnderecoSerializer, PedidoSerializer

from rest_framework.decorators import api_view

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        # colocar username dentro do colchetes e após o ponto colocar username
        token['nome'] = user.nome
        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class IsAuthenticatedOrPostOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # Permitir POST requests mesmo se o usuário não estiver autenticado
        elif request.method == 'POST':
            return True
        return False


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
   # permission_classes = [IsAuthenticatedOrPostOnly,]

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class LoginWithPhoneOTP(APIView):
    def post(self, request):

        celular = request.data.get('celular', '')

        try:
            user = Usuario.objects.get(celular=celular)

        except Usuario.DoesNotExist:
            return Response({'error_no_phone_account': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp_phone(celular, otp)

        return Response({'error_no_email_account': 'OTP has been sent to your phone number.', 'success': True}, status=status.HTTP_200_OK)


class ValidateOTP(APIView):
    def post(self, request):

        # email = request.data.get('email', '')
        otp = request.data.get('otp', '')

        try:
            user = Usuario.objects.get(otp=otp)

        except Usuario.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if user.otp == otp:
            user.otp = None  # Reset the OTP field after successful validation
            user.save()

            # Authenticate the user and create or get an authentication token
            # token, _ = Token.objects.get_or_create(user=user)

            user_data = {
                'token': 1
            }

            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_produtos_restaurantes(request, id_restaurante):
    
    produtos = Produto.objects.filter(restaurante = id_restaurante)

    product_s = ProdutoSerializer(instance=produtos ,many=True)

    return Response(product_s.data, status=status.HTTP_200_OK)
