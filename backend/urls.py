"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from back_delivery.models import Endereco
from back_delivery.views import MyTokenObtainPairView, UsuarioViewSet, ProdutoViewSet, RestauranteViewSet, EnderecoViewSet, get_produtos_restaurantes
from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from back_delivery.views import LoginWithPhoneOTP, ValidateOTP
from django.conf import settings
from django.conf.urls.static import static

def send_email_confirmation(request):
    msg_1 = EmailMultiAlternatives(
        'Confirmação de pedido!',
        'Este é um email de confirmação de pedido, agora falta pouco para você completar a compra!',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_1.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
def send_email_preparing(request):
    msg_2 = EmailMultiAlternatives(
        'Pedido sendo preparado!',
        'Este é um email de confirmação, seu pedido está sendo preparado',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_2.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
def send_email_awaiting_payment(request):
    msg_3 = EmailMultiAlternatives(
        'Aguardando pagamento!',
        'Este é um email de confirmação, estamos aguardando o seu pagamento.',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_3.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
def send_email_confirmed_payment(request):
    msg_4 = EmailMultiAlternatives(
        'Pagamento confirmado!',
        'Este é um email de confirmação, seu pagamento foi confirmado, logo entrará em separação.',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_4.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
    
def send_email_separation(request):
    msg_5 = EmailMultiAlternatives(
        'Pedido em separação!',
        'Este é um email de confirmação, seu pedido está em separação!',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_5.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
def send_email_invoiced(request):
    msg_6 = EmailMultiAlternatives(
        'Pedido faturado!',
        'Este é um email de confirmação, seu pedido foi faturado!',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_6.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
def send_email_transportation(request):
    msg_7 = EmailMultiAlternatives(
        'Saiu para entrega!',
        'Este é um email de confirmação, seu pedido saiu para entrega!',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_7.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)
    
def send_email_finish(request):
    msg_8 = EmailMultiAlternatives(
        'Pedido concluido!',
        'Este é um email de confirmação, seu pedido foi concluído!',
       'dls185568@gmail.com',
       #'luarabisqui@gmail.com'
       ['derekoob@hotmail.com',],#'san.25alm@gmail.com.br','luarabisqui@gmail.com']
    )

    try:
        num_sent = msg_8.send()
    except Exception as e:
        return HttpResponse(f'Erro ao enviar e-mail: {str(e)}', status=500)

    if num_sent:
        return HttpResponse('E-mail enviado com sucesso!')
    else:
        return HttpResponse('Falha ao enviar e-mail.', status=500)




router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'produtos',ProdutoViewSet)
router.register(r'restaurantes',RestauranteViewSet)
router.register(r'enderecos',EnderecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirmar/', send_email_confirmation),
    path('pedido-finalizado/', send_email_preparing),
    path('pedido-aguardando/', send_email_awaiting_payment),
    path('pedido-pagamento-confirmado/', send_email_confirmed_payment),
    path('pedido-separacao/', send_email_separation),
    path('pedido-faturado/', send_email_invoiced),
    path('pedido-entrega/', send_email_transportation),
    path('pedido-concluido/', send_email_finish),
    path('otp/', LoginWithPhoneOTP.as_view(), name='login-with-otp'),
    path('validate-otp/', ValidateOTP.as_view(), name='validate-otp'),
    
    path('restaurantes-produtos/<int:id_restaurante>/', get_produtos_restaurantes, name='restaurantes-produtos'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    