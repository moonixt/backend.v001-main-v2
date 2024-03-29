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
from back_delivery.views import MyTokenObtainPairView, UsuarioViewSet, ProdutoViewSet, RestauranteViewSet, get_produtos_restaurantes
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





def send_email(request):
    msg = EmailMultiAlternatives(
        'Email de teste',
        'Este é um email de confirmação teste',
       #email do projeto 'dls185568@gmail.com',
       #email pessoal ['@hotmail.com']
    )

    msg.send()

    try:
        num_sent = msg.send()
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

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('testmail/', send_email),
    path('otp/', LoginWithPhoneOTP.as_view(), name='login-with-otp'),
    path('validate-otp/', ValidateOTP.as_view(), name='validate-otp'),
    
    path('restaurantes-produtos/<int:id_restaurante>/', get_produtos_restaurantes, name='restaurantes-produtos'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    