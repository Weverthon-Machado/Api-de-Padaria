from django.contrib import admin

from django.contrib import admin

from Cliente.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf','sexo', 'endereco','telefone', 'email', 'data_nascimento', 'codigo_cliente')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(Cliente, Clientes)