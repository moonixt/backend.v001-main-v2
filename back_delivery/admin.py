from django.contrib import admin

from .models import Endereco, Item_pedido, Pagamento, Pedido, Produto, Usuario

admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Pedido)
admin.site.register(Item_pedido)
admin.site.register(Produto)
admin.site.register(Pagamento)
