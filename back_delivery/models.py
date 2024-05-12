from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, nome, password, **other):

        if not email:
            raise ValueError("You must provide an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **other)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, nome, password, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, nome, password, **other)


# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=50, null=False,
                            blank=False, unique=True)
    cpf = models.CharField(max_length=12, null=True, blank=True)
    celular = models.CharField(max_length=16, null=False, blank=False)
    email = models.CharField(max_length=50, null=False,
                             blank=False, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.SmallIntegerField(blank=False)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    ponto_ref = models.CharField(max_length=50, null=True, blank=True)
    # bairro = models.CharField(max_length=50, null=False, blank=False)
    # cidade = models.CharField(max_length=50, null=False, blank=False)
    # uf = models.CharField(max_length=2, null=False, blank=False)
    # endereco_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.logradouro


class Pedido(models.Model):
    num_nota_fiscal = models.IntegerField()
    serie_nota_fiscal = models.IntegerField()
    data_compra = models.DateTimeField(auto_now=False, auto_now_add=False)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_total = models.IntegerField()
    pedido_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome_categoria


class Restaurante(models.Model):
    image = models.ImageField(upload_to='upload/images',null=False, blank=True)
    nome_restaurante = models.CharField(max_length=50, null=False, blank=False)
    logradouro_restaurante = models.CharField(
        max_length=50, null=False, blank=False)
    numero_restaurante = models.SmallIntegerField(blank=False)
    complemento_restaurante = models.CharField(
        max_length=50, blank=True, null=True)
    ponto_ref_restaurante = models.CharField(
        max_length=50, null=True, blank=True)
    bairro_restaurante = models.CharField(
        max_length=50, null=False, blank=False)
    cidade_restaurante = models.CharField(
        max_length=50, null=False, blank=False)
    uf_restaurante = models.CharField(max_length=2, null=False, blank=False)
    cep_restaurante = models.CharField(max_length=7, null=False, blank=False)
    descricao_restaurante = models.TextField(null=True, blank=True)
    categoria_restaurante = models.ForeignKey(
        Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_restaurante


class Produto(models.Model):
    image = models.ImageField(
    upload_to='upload/images', null=True, blank=True)
    nome_produto = models.CharField(max_length=50, null=False, blank=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    qtd_estoque = models.IntegerField(blank=True)
    descricao = models.TextField(null=False, blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto


class Item_pedido(models.Model):
    valor_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    qtd = models.IntegerField()
    valor_desconto = models.IntegerField()
    pedido = models.ForeignKey(
        Produto, related_name='itens', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Pagamento(models.Model):
    num_cartao = models.IntegerField()
    nome_cartao = models.CharField(max_length=50, null=False, blank=False)
    validade = models.DateField()
    cvv = models.SmallIntegerField()
    pag_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cartao
