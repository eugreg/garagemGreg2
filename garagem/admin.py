from django.contrib import admin

from garagem.models import Marca, Categoria,Veiculos, Cor, Acessorio

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Veiculos)
admin.site.register(Cor)
admin.site.register(Acessorio)

